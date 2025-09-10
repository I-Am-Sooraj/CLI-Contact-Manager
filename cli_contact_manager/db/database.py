import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "contacts.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        """CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE
        );"""
    )
    return conn
