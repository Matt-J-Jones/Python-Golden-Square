from lib.contact_list import ContactList

def test_creates_object():
    contact_list = ContactList()
    assert isinstance(contact_list, ContactList)

def adds_contact_to_list():
    contact_list = ContactList()
    contact_list.add_contact(["Test", 1234])
    assert isinstance(contact_list, ContactList)

def adds_contact_to_list_returns_list():
    contact_list = ContactList()
    contact_list.add_contact(["Test", 1234])
    assert contact_list.return_formatted_contacts() == "Test: 1234"

def adds__two_contact_to_list_returns_list():
    contact_list = ContactList()
    contact_list.add_contact(["Test_1", 1234])
    contact_list.add_contact(["Test_2", 5678])
    assert contact_list.return_formatted_contacts() == "Test_1: 1234\nTest_2: 4567"