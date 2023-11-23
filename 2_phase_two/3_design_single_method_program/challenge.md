# ToDo Checker Function Design Recipe

## 1. Describe the Problem

```html
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
```

## 2. Design the Function Signature

```python
# EXAMPLE

def grammar_checker(str):
    """returns True if text includes the string '#TODO'

    Parameters: (list all parameters and their types)
        str: a string containing words (e.g. "#TODO: Hello world!")

    Returns: a bool
    """
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a string starting with todo, returns True
"""
grammar_checker("#TODO Hello, world.") => True

"""
Given a string containing todo, returns True
"""
grammar_checker("Hello #TODO world.") => True

"""
Given a string not containing todo, returns False
"""
grammar_checker("hello, world.") => False

"""
Given an empty string, returns an error
"""
grammar_checker("") => "Cannot check empty string."
```

## 4. Implement the Behaviour