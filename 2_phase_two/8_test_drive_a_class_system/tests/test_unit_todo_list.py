from lib.todo_list import TodoList

def test_creates_object():
    todolist = TodoList()
    assert isinstance(todolist, TodoList)
