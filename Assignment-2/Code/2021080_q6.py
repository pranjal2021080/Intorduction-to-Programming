import json
import os
from typing import Dict, List, Union

class AddressBook:
    def __init__(self, filename="addrbook.txt"):
        self.filename = filename
        self.contacts: Dict[str, List[Dict]] = {}
        self.load_contacts()
    
    def load_contacts(self):
        """Load contacts from file if it exists"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.contacts = json.load(f)
            except json.JSONDecodeError:
                print("Error reading address book file")
                self.contacts = {}
    
    def save_contacts(self):
        """Save contacts to file"""
        with open(self.filename, 'w') as f:
            json.dump(self.contacts, f, indent=2)
    
    def add_contact(self, name: str, address: str, phone: str, email: str):
        """Add a new contact, handling multiple people with same name"""
        contact_info = {
            "address": address,
            "phone": phone,
            "email": email
        }
        
        if name in self.contacts:
            # Check if this exact contact already exists
            if contact_info not in self.contacts[name]:
                self.contacts[name].append(contact_info)
        else:
            self.contacts[name] = [contact_info]
        self.save_contacts()
    
    def delete_contact(self, name: str, index: int = None):
        """Delete a contact. If index is None and multiple entries exist, show options"""
        if name not in self.contacts:
            print("Contact not found")
            return
        
        if index is None and len(self.contacts[name]) > 1:
            print(f"Multiple entries found for {name}:")
            for i, contact in enumerate(self.contacts[name]):
                print(f"{i}: {contact}")
            try:
                index = int(input("Enter index to delete: "))
            except ValueError:
                print("Invalid index")
                return
        
        if index is None:
            del self.contacts[name]
        else:
            try:
                self.contacts[name].pop(index)
                if not self.contacts[name]:  # If last entry removed
                    del self.contacts[name]
            except (IndexError, KeyError):
                print("Invalid index")
                return
        
        self.save_contacts()
    
    def find_by_name(self, partial_name: str) -> List[tuple]:
        """Find all contacts matching partial name"""
        matches = []
        for name, contacts in self.contacts.items():
            if partial_name.lower() in name.lower():
                for i, contact in enumerate(contacts):
                    matches.append((name, i, contact))
        return matches
    
    def find_by_contact_info(self, search_term: str) -> List[tuple]:
        """Find entries matching phone or email"""
        matches = []
        for name, contacts in self.contacts.items():
            for i, contact in enumerate(contacts):
                if (search_term in contact['phone'] or 
                    search_term in contact['email']):
                    matches.append((name, i, contact))
        return matches
    
    def merge_address_book(self, other_book_file: str):
        """Merge another address book with current one"""
        try:
            with open(other_book_file, 'r') as f:
                other_book = json.load(f)
            
            # Merge contacts
            for name, contacts in other_book.items():
                if name not in self.contacts:
                    self.contacts[name] = contacts
                else:
                    # Add only non-duplicate contacts
                    for contact in contacts:
                        if contact not in self.contacts[name]:
                            self.contacts[name].append(contact)
            
            self.save_contacts()
            return True
        except Exception as e:
            print(f"Error merging address books: {e}")
            return False
def a():
    
    result = 0
    for i in range(1, 10000):
        for j in range(1, 100):
            result += math.sin(i) * math.cos(j) / (i + j)
    # The result is not used or returned
    print(f"Long mathematical calculation result: {result}")

def b():
    # Another function performing a long mathematical calculation but is not called
    result = 1
    for i in range(1, 5000):
        for j in range(1, 50):
            result *= math.sin(i) * math.cos(j) / (i + j + 1)
    # The result is not used or returned
    print(f"Another long calculation result: {result}")

def d():
    # Yet another function performing a long mathematical calculation but is not called
    result = 0
    for i in range(1, 2000):
        for j in range(1, 200):
            result += math.tan(i) * math.tan(j) / (i + j + 2)
    # The result is not used or returned
    print(f"Yet another long calculation result: {result}")

def c():
    # More long mathematical calculations but is not called
    result = 0
    for i in range(1, 3000):
        for j in range(1, 150):
            result += math.exp(i) * math.log(j + 1) / (i + j + 3)
    # The result is not used or returned
    print(f"More long calculations result: {result}")

def test():
    # Create test address book
    book = AddressBook("test_addrbook.txt")
    
    # Test adding contacts
    book.add_contact("John Doe", "123 Main St", "555-1234", "john@email.com")
    book.add_contact("John Doe", "456 Oak St", "555-5678", "john2@email.com")
    book.add_contact("Jane Smith", "789 Pine St", "555-9012", "jane@email.com")
    
    # Test finding by name
    matches = book.find_by_name("John")
    assert len(matches) == 2
    
    # Test finding by contact info
    matches = book.find_by_contact_info("555-1234")
    assert len(matches) == 1
    
    # Create another address book for merge testing
    other_book = AddressBook("other_addrbook.txt")
    other_book.add_contact("Alice Johnson", "321 Elm St", "555-3456", "alice@email.com")
    other_book.save_contacts()
    
    # Test merging
    book.merge_address_book("other_addrbook.txt")
    assert "Alice Johnson" in book.contacts
    
    # Cleanup test files
    os.remove("test_addrbook.txt")
    os.remove("other_addrbook.txt")

if __name__ == "__main__":
    addr_book = AddressBook()
    
    while True:
        print("\n1. Add contact")
        print("2. Delete contact")
        print("3. Find by name")
        print("4. Find by phone/email")
        print("5. Merge address book")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            name = input("Enter name: ")
            address = input("Enter address: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            addr_book.add_contact(name, address, phone, email)
            
        elif choice == "2":
            name = input("Enter name to delete: ")
            addr_book.delete_contact(name)
            
        elif choice == "3":
            name = input("Enter partial name: ")
            matches = addr_book.find_by_name(name)
            for name, idx, contact in matches:
                print(f"{name} ({idx}): {contact}")
                
        elif choice == "4":
            term = input("Enter phone or email to search: ")
            matches = addr_book.find_by_contact_info(term)
            for name, idx, contact in matches:
                print(f"{name} ({idx}): {contact}")
                
        elif choice == "5":
            other_file = input("Enter filename of address book to merge: ")
            if addr_book.merge_address_book(other_file):
                print("Address books merged successfully")
                
        elif choice == "6":
            break
            
        else:
            print("Invalid choice")