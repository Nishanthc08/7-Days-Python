import json

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                self.contacts = json.load(file)
        except FileNotFoundError:
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file)

    def add_contact(self, name, phone, email):
        self.contacts.append({"name": name, "phone": phone, "email": email})
        self.save_contacts()
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. {contact['name']} - {contact['phone']} - {contact['email']}")

    def delete_contact(self, index):
        if 0 < index <= len(self.contacts):
            removed_contact = self.contacts.pop(index - 1)
            self.save_contacts()
            print(f"Contact '{removed_contact['name']}' removed.")
        else:
            print("Invalid contact number.")

contact_book = ContactBook()

while True:
    print("\nContact Book Options:")
    print("1. View contacts")
    print("2. Add contact")
    print("3. Delete contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        contact_book.view_contacts()
    elif choice == '2':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        contact_book.add_contact(name, phone, email)
    elif choice == '3':
        index = int(input("Enter contact number to delete: "))
        contact_book.delete_contact(index)
    elif choice == '4':
        print("Exiting the Contact Book.")
        break
    else:
        print("Invalid choice, please choose again.")
