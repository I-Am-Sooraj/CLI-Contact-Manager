# CLI Contact Manager

A simple command-line contact manager using SQLite.

## Features
- Add, list, search, and delete contacts
- Update email for a contact
- Stores data in a local SQLite database

## Project Structure
```
CLI-Contact-Manager/
├─ cli_contact_manager/
│  ├─ cli/
│  │  ├─ main.py        # Entry point and menu
│  │  └─ menu.py        # CLI menu rendering and input handling
│  ├─ db/
│  │  └─ database.py    # SQLite connection and schema
│  └─ services/
│     ├─ __init__.py
│     └─ contacts_service.py  # CRUD operations
├─ contacts.py          # Legacy runner that delegates to package entry
├─ .gitignore
├─ LICENSE
└─ README.md
```

## Quick start
Run with Python 3.9+:

```powershell
# Option A: Run as module from source
python -m cli_contact_manager.cli.main

# Option B: Install editable and use console script
pip install -e .
contacts
```

A `contacts.db` file will be created automatically on first run (under `cli_contact_manager/`).

## Notes
- Phone and email must be unique.
- The database path is `cli_contact_manager/contacts.db` relative to the package. Update `DB_PATH` in `database.py` if you prefer a different location.

## License
MIT – see `LICENSE`.
