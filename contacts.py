import sqlite3

# connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('contacts.db')

# create a new table to store contacts if it doesn't exist
conn.execute('''CREATE TABLE IF NOT EXISTS contacts 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NAME TEXT NOT NULL,
                 PHONE TEXT NOT NULL UNIQUE,
                 EMAIL TEXT NOT NULL UNIQUE);''')

def add_contact():
    print("Enter contact details:")
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    try:
        conn.execute("INSERT INTO contacts (NAME, PHONE, EMAIL) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        print("Contact added successfully.")
    except sqlite3.IntegrityError:
        print("Contact with the same phone number or email already exists.")

def view_contacts():
    cursor = conn.execute("SELECT * FROM contacts")
    rows = cursor.fetchall()
    
    print("ID\tNAME\t\t\tPHONE\t\t\tEMAIL")
    print("-" * 70)
    for row in rows:
        print(f"{row[0]}\t{row[1]:<20}\t{row[2]:<20}\t{row[3]:<30}")
        
def remove_contact():
    id = input("Enter ID of the contact to be removed: ")
    
    try:
        conn.execute("DELETE FROM contacts WHERE ID=?", (id,))
        conn.commit()
        print("Contact removed successfully.")
    except sqlite3.IntegrityError:
        print("Invalid ID. No contact found with the given ID.")
        
def search_contact():
    cursor = conn.cursor()
    search_term = input("Enter name or phone number to search: ")
    cursor.execute("SELECT * FROM contacts WHERE NAME LIKE ? OR PHONE LIKE ?", (f"%{search_term}%", f"%{search_term}%"))
    results = cursor.fetchall()
    if not results:
        print("No matching contacts found.")
    else:
        print("ID\tNAME\t\t\tPHONE\t\t\tEMAIL")
        print("-" * 70)
        for row in results:
            print(f"{row[0]}\t{row[1]:<20}\t{row[2]:<20}\t{row[3]:<30}")


def add_email():
    id = input("Enter ID of the contact to add email: ")
    email = input("Enter email to be added: ")
    
    try:
        conn.execute("UPDATE contacts SET EMAIL=? WHERE ID=?", (email, id))
        conn.commit()
        print("Email added successfully.")
    except sqlite3.IntegrityError:
        print("Invalid ID. No contact found with the given ID.")
        
# main program loop
while True:
    print("\n")
    print("=" * 20, "CONTACT MANAGER", "=" * 20)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Remove Contact")
    print("4. Search Contact")
    print("5. Add Email")
    print("6. Exit")
    print("=" * 51)
    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()

    elif choice == '2':
        view_contacts()

    elif choice == '3':
        remove_contact()

    elif choice == '4':
        search_contact()

    elif choice == '5':
        add_email()

    elif choice == '6':
        conn.close()
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")

# Close the database connection if it's still open (may already be closed above)
conn.close()
#close the database connection
# conn.close()  # Removed redundant close; already handled on exit
