from lib.menu_item import MenuItem
from lib.takeaway import Takeaway
import pytest

Menu_item_one = MenuItem("Rice", 1.5, True)
Menu_item_two = MenuItem("Coke", 0.9, False)

def test_adds_item_to_menu():
    takeaway = Takeaway()
    takeaway.add_item(Menu_item_one)
    assert takeaway.return_menu() == "1: Rice: £1.50, Available"

def test_adds_multiple_items_to_menu():
    takeaway = Takeaway()
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_two)
    assert takeaway.return_menu() == "1: Rice: £1.50, Available\n2: Coke: £0.90, Sold Out"

def test_adds_items_returns_order():
    takeaway = Takeaway()
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_two)
    takeaway.add_item_to_order(Menu_item_one)
    takeaway.add_item_to_order(Menu_item_one)
    takeaway.add_item_to_order(Menu_item_two)
    assert len(takeaway.return_order()) == 2

def test_adds_items_returns_confirmation():
    takeaway = Takeaway()
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_two)
    takeaway.add_item_to_order(Menu_item_one)
    takeaway.add_item_to_order(Menu_item_one)
    takeaway.add_item_to_order(Menu_item_two)
    assert takeaway.confirm_order() == "Rice, Rice - Total: £3.00"

def test_adds_items_returns_confirmation_text():
    takeaway = Takeaway()
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_one)
    takeaway.add_item(Menu_item_two)
    takeaway.add_item_to_order(Menu_item_one)
    takeaway.add_item_to_order(Menu_item_one)
    takeaway.add_item_to_order(Menu_item_two)
    assert takeaway.confirm_order() == "Rice, Rice - Total: £3.00"
    assert takeaway.tracking_and_confirmation() is True
