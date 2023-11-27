from lib.todo import Todo
from lib.todo_list import TodoList

def test_creates_objects():
    todo = Todo("Buy Milk")
    todolist = TodoList()
    assert isinstance(todo, Todo)
    assert isinstance(todolist, TodoList)

def test_adds_new_item_to_list():
    todo = Todo("Buy Milk")
    todolist = TodoList()
    todolist.add(todo)

def test_adds_item_returns_formatted_list():
    todo_1 = Todo("Buy Milk")
    todolist = TodoList()
    todolist.add(todo_1)
    assert todolist.all() == "Buy Milk - Incomplete"

def test_adds_items_returns_formatted_list():
    todo_1 = Todo("Buy Milk")
    todo_2 = Todo("Walk Dog")
    todo_2.mark_complete()
    todolist = TodoList()
    todolist.add(todo_1)
    todolist.add(todo_2)
    assert todolist.all() == "Buy Milk - Incomplete\nWalk Dog - Complete"

def test_adds_item_returns_list_of_incomplete():
    todo_1 = Todo("Buy Milk")
    todo_2 = Todo("Walk Dog")
    todo_2.mark_complete()
    todolist = TodoList()
    todolist.add(todo_1)
    todolist.add(todo_2)
    assert todolist.incomplete() == "Buy Milk - Incomplete"

def test_adds_item_returns_list_of_complete():
    todo_1 = Todo("Buy Milk")
    todo_2 = Todo("Walk Dog")
    todo_2.mark_complete()
    todolist = TodoList()
    todolist.add(todo_1)
    todolist.add(todo_2)
    assert todolist.complete() == "Walk Dog - Complete"

def test_adds_items_marks_all_as_complete():
    todo_1 = Todo("Buy Milk")
    todo_2 = Todo("Walk Dog")
    todolist = TodoList()
    todolist.add(todo_1)
    todolist.add(todo_2)
    assert todolist.all() == "Buy Milk - Incomplete\nWalk Dog - Incomplete"
    todolist.give_up()
    assert todolist.all() == "Buy Milk - Complete\nWalk Dog - Complete"
    assert todolist.complete() == "Buy Milk - Complete\nWalk Dog - Complete"
