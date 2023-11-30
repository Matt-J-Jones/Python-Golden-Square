from lib.takeaway import Takeaway
import pytest
from unittest.mock import Mock

def test_creates_object():
    takeaway = Takeaway()
    assert isinstance(takeaway, Takeaway)