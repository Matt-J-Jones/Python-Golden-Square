from lib.todo import Todo

def test_creates_object():
    todo = Todo("Buy Milk")
    assert isinstance(todo, Todo)
