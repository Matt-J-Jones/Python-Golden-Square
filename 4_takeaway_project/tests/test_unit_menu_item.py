from lib.menu_item import MenuItem
import pytest

def test_creates_object():
    menu_item = MenuItem("example item", 9.99, True)
    assert isinstance(menu_item, MenuItem)

def test_returns_formatted_item_available():
    menu_item = MenuItem("example item", 9.99, True)
    assert menu_item.return_formatted_item() == "example item: £9.99, Available"

def test_returns_formatted_item_unavailable():
    menu_item = MenuItem("example item", 9.99, False)
    assert menu_item.return_formatted_item() == "example item: £9.99, Sold Out"

def test_adds_item_marks_sold_out():
    menu_item = MenuItem("example item", 9.99, True)
    assert menu_item.return_formatted_item() == "example item: £9.99, Available"
    menu_item.mark_sold_out()
    assert menu_item.return_formatted_item() == "example item: £9.99, Sold Out"

def test_returns_formatted_item_with_2_decimal_places():
    menu_item = MenuItem("example item", 9.00, False)
    assert menu_item.return_price_as_string() == "9.00"

def test_returns_item_name_price_availability_individually():
    menu_item = MenuItem("example item", 1.01, False)
    assert menu_item.return_price_as_string() == "1.01"
    assert menu_item.return_name() == "example item"
    assert menu_item.return_status() == "Sold Out"
    assert menu_item.return_price() == 1.01
