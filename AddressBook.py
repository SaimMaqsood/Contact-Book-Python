import json
import os

"""
A class that manages a collection of contacts with CRUD operations and JSON persistence.
"""
class AddressBook:
    """
    Constructs an address book, loading from file if it exists.
    @param filename the JSON file to save/load from
    """
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Contact(**c) for c in data]
        return []

    def save(self):
        with open(self.filename, 'w') as f:
            data = [{"name": c.name, "phone": c.phone, "email": c.email} for c in self.contacts]
            json.dump(data, f, indent=2)
        print("Contacts saved.")

    def add_contact(self, name, phone, email=""):
        if name and phone:
            contact = Contact(name, phone, email)
            self.contacts.append(contact)
            print(f"Added: {contact}")
            self.save()
        else:
            print("Name and phone are required.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts yet.")
            return
        for i, c in enumerate(self.contacts, 1):
            print(f"{i}. {c}")

    def search(self, term):
        found = [c for c in self.contacts if term.lower() in c.name.lower() or term in c.phone]
        if found:
            for c in found:
                print(c)
        else:
            print("No matches found.")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                print(f"Deleted: {c}")
                self.save()
                return
        print("Contact not found.")
