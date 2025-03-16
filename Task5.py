import json

CONTACTS_FILE = "contacts.json"

def load():
    
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_c(contacts):
    
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def add_c():

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts = load()
    contacts[name] = {"phone": phone, "email": email, "address": address}
    save_c(contacts)
    print(f"Contact {name} added successfully!")

def view_c():
    
    contacts = load()
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"{name}: {details['phone']}")

def search_c():
    
    query = input("Enter name or phone number to search: ").strip()
    contacts = load()

    found = False
    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details["phone"]:
            print(f"\nName: {name}\nPhone: {details['phone']}\nEmail: {details['email']}\nAddress: {details['address']}\n")
            found = True
    
    if not found:
        print("Contact not found.")

def update_c():
    
    name = input("Enter the contact name to update: ").strip()
    contacts = load()

    if name in contacts:
        phone = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        address = input("Enter new address: ").strip()
        contacts[name] = {"phone": phone, "email": email, "address": address}
        save_c(contacts)
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found.")

def delete_c():
    
    name = input("Enter the contact name to delete: ").strip()
    contacts = load()

    if name in contacts:
        del contacts[name]
        save_c(contacts)
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found.")

def main():

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_c()
        elif choice == "2":
            view_c()
        elif choice == "3":
            search_c()
        elif choice == "4":
            update_c()
        elif choice == "5":
            delete_c()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
