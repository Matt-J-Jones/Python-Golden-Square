from lib.todo import ToDo
import pytest

def test_creates_object():
    todo = ToDo()
    assert isinstance(todo, ToDo)

def test_print_empty_list():
    todo = ToDo()
    assert todo.print_list() == ""

def test_add_item_to_list_print_list_of_one():
    todo = ToDo()
    todo.add("Walk the Dog")
    assert todo.print_list() == "Walk the Dog"

def test_add_two_items_to_list_print_list_of_two():
    todo = ToDo()
    todo.add("Walk the Dog")
    todo.add("Buy Milk")
    assert todo.print_list() == "Walk the Dog, Buy Milk"

def test_add_three_items_to_list_mark_one_complete_print_list_of_two():
    todo = ToDo()
    todo.add("Walk the Dog")
    todo.add("Buy Milk")
    todo.add("Have a Nap")
    todo.mark_complete("Buy Milk")
    assert todo.print_list() == "Walk the Dog, Have a Nap"

def test_raises_error_if_blank_task_is_added():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add("")
    error_message = str(e.value)
    assert error_message == "Task cannot be empty"

def test_raises_error_if_none_task_is_added():
    todo = ToDo()
    with pytest.raises(Exception) as e:
        todo.add(None)
    error_message = str(e.value)
    assert error_message == "Task cannot be empty"
