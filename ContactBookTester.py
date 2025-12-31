from AddressBook import AddressBook

"""
This program tests the AddressBook class with an interactive menu.
"""
class ContactBookTester:
    @staticmethod
    def main():
        book = AddressBook()

        while True:
            print("\nContact Book Menu")
            print("1. Add contact")
            print("2. View all contacts")
            print("3. Search contact")
            print("4. Delete contact")
            print("5. Exit")
            choice = input("Choose: ").strip()

            if choice == '1':
                name = input("Name: ").strip()
                phone = input("Phone: ").strip()
                email = input("Email (optional): ").strip()
                book.add_contact(name, phone, email)
            elif choice == '2':
                book.view_contacts()
            elif choice == '3':
                term = input("Search term (name or phone): ").strip()
                book.search(term)
            elif choice == '4':
                name = input("Name to delete: ").strip()
                book.delete_contact(name)
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    ContactBookTester.main()
