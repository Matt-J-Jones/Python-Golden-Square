from lib.menu_item import MenuItem
import pytest

def test_creates_object():
    menu_item = MenuItem()
    assert isinstance(menu_item, MenuItem)