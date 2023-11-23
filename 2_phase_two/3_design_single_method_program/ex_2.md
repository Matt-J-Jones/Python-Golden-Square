# Grammar Checker Function Design Recipe

## 1. Describe the Problem

```html
As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.
```

## 2. Design the Function Signature

```python
# EXAMPLE

def grammar_checker(str):
    """returns True if sentence starts with capital letter and ends with punctuation

    Parameters: (list all parameters and their types)
        str: a string containing words (e.g. "Hello world!")

    Returns: a bool
    """
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a string containing correct grammar, returns True
"""
grammar_checker("Hello, world.") => True

"""
Given a string containing incorrect grammar, returns False
"""
grammar_checker("hello, world.") => False

"""
Given an empty string, returns an error
"""
grammar_checker("") => "Cannot check grammar for an empty string."
```

## 4. Implement the Behaviour
