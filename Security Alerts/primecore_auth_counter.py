#!/usr/bin/env python3
"""Lab detector: five consecutive observed wrong-password events per domain user."""
import argparse
import hashlib
import json
import os
import sqlite3
import subprocess
from datetime import datetime, timezone
from pathlib import Path


class Counter:
    def __init__(self, database, output):
        self.output = Path(output)
        self.db = sqlite3.connect(database)
        self.db.executescript('''
            CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT);
            CREATE TABLE IF NOT EXISTS seen (id TEXT PRIMARY KEY);
            CREATE TABLE IF NOT EXISTS users (id TEXT PRIMARY KEY, failures INTEGER);
            CREATE TABLE IF NOT EXISTS outbox (id INTEGER PRIMARY KEY, body TEXT, sent INTEGER DEFAULT 0);
        ''')
        with self.db:
            self.db.execute("INSERT OR IGNORE INTO settings VALUES ('start', ?)",
                            (datetime.now(timezone.utc).isoformat(),))
        self.start = datetime.fromisoformat(self.db.execute(
            "SELECT value FROM settings WHERE key='start'").fetchone()[0])

    def process(self, line):
        try:
            raw = line[line.index('{'):]
            event = json.loads(raw)
            if event.get('type') != 'Authentication':
                return
            data = event['Authentication']
            status = data.get('status')
            if status not in ('NT_STATUS_OK', 'NT_STATUS_WRONG_PASSWORD'):
                return
            timestamp = datetime.fromisoformat(event['timestamp'].replace('Z', '+00:00'))
            if timestamp < self.start:
                return
            user = data.get('mappedAccount') or data.get('becameAccount')
            domain = data.get('mappedDomain') or data.get('becameDomain')
            if not user or not domain or user.endswith('$'):
                return
            key = (domain + '\\' + user).casefold()
            identity = hashlib.sha256(json.dumps(event, sort_keys=True).encode()).hexdigest()
        except (ValueError, KeyError, TypeError):
            return
        with self.db:
            if self.db.execute('INSERT OR IGNORE INTO seen VALUES (?)', (identity,)).rowcount == 0:
                return
            previous = self.db.execute('SELECT failures FROM users WHERE id=?', (key,)).fetchone()
            count = 0 if status == 'NT_STATUS_OK' else (previous[0] if previous else 0) + 1
            self.db.execute('INSERT OR REPLACE INTO users VALUES (?, ?)', (key, count))
            if count == 5:
                alert = dict(event='consecutive_password_failures', user=user.casefold(),
                             domain=domain.casefold(), failures=5,
                             source=data.get('remoteAddress'), service=data.get('serviceDescription'),
                             dc='hq-dc-01', authentication_time=event['timestamp'],
                             detected_at=datetime.now(timezone.utc).isoformat(), event_id=identity)
                self.db.execute('INSERT INTO outbox(body) VALUES (?)', (json.dumps(alert),))
        self.flush()

    def flush(self):
        for number, body in self.db.execute('SELECT id, body FROM outbox WHERE sent=0').fetchall():
            with self.output.open('a', encoding='utf-8') as stream:
                stream.write(body + '\n')
                stream.flush()
                os.fsync(stream.fileno())
            with self.db:
                self.db.execute('UPDATE outbox SET sent=1 WHERE id=?', (number,))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='/var/log/samba-auth.log')
    parser.add_argument('--database', default='/var/lib/primecore-auth/counter.sqlite')
    parser.add_argument('--output', default='/var/log/primecore-auth-alerts.log')
    args = parser.parse_args()
    Path(args.database).parent.mkdir(parents=True, exist_ok=True)
    counter = Counter(args.database, args.output)
    counter.flush()
    # Replay retained lines after restart; persistent fingerprints prevent recounting.
    process = subprocess.Popen(['tail', '-n', '+1', '-F', args.input],
                               stdout=subprocess.PIPE, text=True, encoding='utf-8', errors='replace')
    try:
        for line in process.stdout:
            counter.process(line)
        raise RuntimeError('Log follower stopped')
    finally:
        process.terminate()
        process.wait()


if __name__ == '__main__':
    main()
