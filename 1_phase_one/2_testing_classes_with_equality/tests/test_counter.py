from lib.counter import Counter

def test_creates_object_returns_zero():
    count = Counter()
    assert count.report() == "Counted to 0 so far."

def test_creates_object_adds_one_returns_1():
    count = Counter()
    count.add(1)
    assert count.report() == "Counted to 1 so far."

def test_creates_object_adds_ten_twice_returns_20():
    count = Counter()
    count.add(10)
    assert count.report() == "Counted to 10 so far."
    count.add(10)
    assert count.report() == "Counted to 20 so far."
    