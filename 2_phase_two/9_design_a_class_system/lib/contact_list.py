class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def return_formatted_contacts(self):
        contacts_to_return = []
        for contact in self.contacts:
            contacts_to_return.append(contact.return_contact())
        return "\n".join(contacts_to_return)