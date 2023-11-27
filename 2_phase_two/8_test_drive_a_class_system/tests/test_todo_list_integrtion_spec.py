from lib.todo import Todo
from lib.todo_list import TodoList

def test_creates_object():
    todo = Todo("Buy Milk")
    todolist = TodoList()
    assert isinstance(todo, Todo)
    assert isinstance(todolist, TodoList)
