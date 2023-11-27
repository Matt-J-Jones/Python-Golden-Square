from lib.contact import Contact
from lib.contact_list import ContactList

def test_adds_object_to_list():
    contact_list = ContactList()
    contact_list.add_contact(Contact(["Test", 1234]))
    assert contact_list.return_formatted_contacts() == "Test: 1234"

def test_adds_multiple_objects_to_list():
    contact_list = ContactList()
    contact_list.add_contact(Contact(["Test", 1234]))
    contact_list.add_contact(Contact(["Test", 5678]))
    contact_list.add_contact(Contact(["Test", 9012]))
    assert contact_list.return_formatted_contacts() == "Test: 1234\nTest: 5678\nTest: 9012"