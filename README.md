# Contact-Book-Python
A simple object-oriented console program for managing contacts.

### What it does
- Add contacts with name, phone, and optional email
- View all contacts
- Search by name or phone
- Delete contacts by name
- Automatically saves/loads contacts to a JSON file
- Basic validation for required fields (name and phone)

### How to run
1. Make sure you have Python installed
2. In the project folder open terminal or command prompt
3. Run the tester program:
   python ContactBookTester.py
 ### Example usage
 Contact Book Menu
1.  Add contact
2.  View all contacts
3.  Search contact
4.  Delete contact
5.  Exit Choose: 1 Name: John Doe Phone: 123-456-7890 Email (optional): john@example.com Added: John Doe | Phone: 123-456-7890 | Email: john@example.com
Choose: 2
1.  John Doe | Phone: 123-456-7890 | Email: john@example.com
### Files
- **Contact.py**  
  Represents a single contact with name, phone, email, and __str__ for printing.

- **AddressBook.py**  
  Manages the list of contacts with add, view, search, delete, and JSON save/load.

- **ContactBookTester.py**  
  Interactive console menu program to test the AddressBook.

Learning project in Python – December 2025
