from ..services.contacts_service import (
    add_contact,
    get_all_contacts,
    delete_contact,
    search_contacts,
    update_email,
    essential_headers,
)


def print_table(rows):
    headers = essential_headers
    print("\t".join(headers))
    print("-" * 70)
    for row in rows:
        print(f"{row[0]}\t{row[1]:<20}\t{row[2]:<20}\t{row[3]:<30}")


def main_menu():
    while True:
        print("\n")
        print("=" * 20, "CONTACT MANAGER", "=" * 20)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Remove Contact")
        print("4. Search Contact")
        print("5. Add/Update Email")
        print("6. Exit")
        print("=" * 51)
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter contact details:")
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            if add_contact(name, phone, email):
                print("Contact added successfully.")
            else:
                print("Contact with the same phone number or email may already exist.")

        elif choice == "2":
            rows = get_all_contacts()
            if rows:
                print_table(rows)
            else:
                print("No contacts yet. Add one from option 1.")

        elif choice == "3":
            id_str = input("Enter ID of the contact to be removed: ")
            if id_str.isdigit() and delete_contact(int(id_str)):
                print("Contact removed successfully.")
            else:
                print("Invalid ID. No contact found with the given ID.")

        elif choice == "4":
            term = input("Enter name or phone number to search: ")
            results = search_contacts(term)
            if results:
                print_table(results)
            else:
                print("No matching contacts found.")

        elif choice == "5":
            id_str = input("Enter ID of the contact to add/update email: ")
            email = input("Enter email to be added: ")
            if id_str.isdigit() and update_email(int(id_str), email):
                print("Email added successfully.")
            else:
                print("Invalid ID. No contact found with the given ID.")

        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")
