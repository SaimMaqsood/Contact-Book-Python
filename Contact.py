"""
A class representing a single contact.
"""
class Contact:
    """
    Constructs a contact with name, phone, and optional email.
    @param name the contact's name
    @param phone the contact's phone number
    @param email the contact's email (optional)
    """
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} | Phone: {self.phone} | Email: {self.email or 'N/A'}"
