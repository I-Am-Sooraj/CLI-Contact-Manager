from typing import Iterable, Tuple
from ..db.database import get_connection


def add_contact(name: str, phone: str, email: str) -> bool:
    conn = get_connection()
    try:
        conn.execute(
            "INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)",
            (name, phone, email),
        )
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        conn.close()


essential_headers = ("ID", "NAME", "PHONE", "EMAIL")


def get_all_contacts() -> Iterable[Tuple[int, str, str, str]]:
    conn = get_connection()
    try:
        cursor = conn.execute("SELECT id, name, phone, email FROM contacts")
        return cursor.fetchall()
    finally:
        conn.close()


def delete_contact(contact_id: int) -> bool:
    conn = get_connection()
    try:
        cur = conn.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()


def search_contacts(term: str) -> Iterable[Tuple[int, str, str, str]]:
    conn = get_connection()
    try:
        cur = conn.execute(
            "SELECT id, name, phone, email FROM contacts WHERE name LIKE ? OR phone LIKE ?",
            (f"%{term}%", f"%{term}%"),
        )
        return cur.fetchall()
    finally:
        conn.close()


def update_email(contact_id: int, email: str) -> bool:
    conn = get_connection()
    try:
        cur = conn.execute("UPDATE contacts SET email=? WHERE id=?", (email, contact_id))
        conn.commit()
        return cur.rowcount > 0
    finally:
        conn.close()
