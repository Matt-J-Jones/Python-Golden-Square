from unittest.mock import Mock, patch
from lib.takeaway import Takeaway
import pytest

example_menu_item_rice = Mock()
example_menu_item_rice.return_formatted_item.return_value = "Rice: £1.50, Available"
example_menu_item_rice.return_status.return_value = "Available"
example_menu_item_rice.return_name.return_value = "Rice"
example_menu_item_rice.return_price.return_value = 1.50

example_menu_item_coke = Mock()
example_menu_item_coke.return_formatted_item.return_value = "Coke: £0.90, Sold Out"
example_menu_item_coke.return_status.return_value = "Sold Out"
example_menu_item_coke.return_name.return_value = "Coke"
example_menu_item_coke.return_price.return_value = 0.90

def test_creates_object():
    takeaway = Takeaway()
    assert isinstance(takeaway, Takeaway)

def test_adds_mock_item_to_menu():
    takeaway = Takeaway()
    takeaway.add_item(example_menu_item_rice)
    assert takeaway.return_menu() == "1: Rice: £1.50, Available"

def test_adds_mock_items_to_menu():
    takeaway = Takeaway()
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_coke)
    assert takeaway.return_menu() == "1: Rice: £1.50, Available\n2: Coke: £0.90, Sold Out"

def test_adds_items_returns_order():
    takeaway = Takeaway()
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_coke)
    takeaway.add_item_to_order(example_menu_item_rice)
    takeaway.add_item_to_order(example_menu_item_rice)
    takeaway.add_item_to_order(example_menu_item_coke)
    assert len(takeaway.return_order()) == 2

def test_adds_items_returns_confirmation():
    takeaway = Takeaway()
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_coke)
    takeaway.add_item_to_order(example_menu_item_rice)
    takeaway.add_item_to_order(example_menu_item_rice)
    takeaway.add_item_to_order(example_menu_item_coke)
    assert takeaway.confirm_order() == "Rice, Rice - Total: £3.00"

@patch('lib.takeaway.keys') 
def test_adds_items_returns_confirmation_text(mock_keys):
    mock_keys = Mock()
    mock_keys.sid.return_value = 'mock_sid'
    mock_keys.token.return_value = 'mock_token'
    mock_keys.to.return_value = 'mock_to'
    mock_keys.sender.return_value = 'mock_sender'
    
    client = Mock()
    client.message.create.return_value = True
    
    takeaway = Takeaway()
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_rice)
    takeaway.add_item(example_menu_item_coke)
    takeaway.add_item_to_order(example_menu_item_rice)
    takeaway.add_item_to_order(example_menu_item_rice)
    takeaway.add_item_to_order(example_menu_item_coke)
    assert takeaway.confirm_order() == "Rice, Rice - Total: £3.00"
    assert takeaway.tracking_and_confirmation(client(mock_keys, mock_keys)) is True