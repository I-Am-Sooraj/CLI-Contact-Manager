"""Legacy entrypoint for the CLI Contact Manager.

This file now delegates to the package entrypoint at
`cli_contact_manager.cli.main:main`.
"""

from cli_contact_manager.cli.main import main


if __name__ == "__main__":
    main()
