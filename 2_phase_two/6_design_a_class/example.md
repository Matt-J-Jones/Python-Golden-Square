# ToDo Class Design Recipe

## 1. Describe the Problem
```
As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.
```

```
As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.
```

## 2. Design the Class Interface

```python
# EXAMPLE

class ToDo:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        # task_list = []
        pass # No code here yet

    def add(self, task)
        # Paramerer: task - string - a task to add to the list
        pass # No code here yet
    
    def print_list(self)
        # prints list of tasks that aren't complete
        pass # No code here yet
    
    def mark_complete(self, task)
        # marks task as complete so it will not appear in the print function
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a task
adds task to list
"""
todo = ToDo()
todo.add("Walk the dog")
todo.print_list() # => "Walk the dog"

"""
Given an empty task, raises error
"""
todo = ToDo()
todo.add() # raises an error with the message "No task to add"

"""
Given list of tasks, returns list of tasks
"""
todo = ToDo()
todo.add("Walk the dog")
todo.add("Buy Milk")
todo.add("Have a Nap")
todo.print_list() # => "Walk the Dog, Buy Milk, Have a Nap"

"""
Given list of tasks, returns list of incomplete tasks
"""
todo = ToDo()
todo.add("Walk the dog")
todo.add("Buy Milk")
todo.add("Have a Nap")
todo.mark_complete("Buy_Milk")
todo.print_list() # => "Walk the Dog, Have a Nap"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
