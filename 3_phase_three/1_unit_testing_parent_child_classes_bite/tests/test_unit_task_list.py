from lib.task_list import TaskList
from unittest.mock import Mock

def test_task_list_initially_empty():
    task_list = TaskList()
    assert task_list.tasks == []


def test_tasks_initially_not_all_complete():
    task_list = TaskList()
    assert task_list.all_complete() == False

def test_adds_mocked_complete_tasks():
    task_list = TaskList()
    fake_task = Mock()
    fake_task.is_complete.return_value = True
    task_list.add(fake_task)
    task_list.add(fake_task)
    assert len(task_list.all()) == 2
    assert task_list.all_complete() is True

def test_adds_mocked_tasks_to_list():
    task_list = TaskList()
    fake_task = Mock()
    fake_task.is_complete.return_value = True
    for x in range(201):
        task_list.add(fake_task)
    assert len(task_list.all()) == 201