from lib.contact import Contact

def test_creates_object():
    contact = Contact(["Test", 1234])
    assert isinstance(contact, Contact)

def test_returns_contact():
    contact = Contact(["Test", 1234])
    assert contact.return_contact() == "Test: 1234"
