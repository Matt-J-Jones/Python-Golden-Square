# Reading Time Estimator Function Design Recipe

## 1. Describe the Problem

```html
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.
```

## 2. Design the Function Signature

```python
# EXAMPLE

def reading_time(str):
    """returns estimated reading time of a string

    Parameters: (list all parameters and their types)
        str: a string containing words (e.g. "hello world")

    Returns: a float containing how long it would take to read the string, in minutes, assuming reading 200wpm
    """
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Given a string containing 200 words, returns a reading time of 1
"""
reading_time("string " * 200) => 1.0

"""
Given a string containing 400 words, returns a reading time of 2
"""
reading_time("string " * 400) => 2.0

"""
Given a string containing 300 words, returns a reading time of 1.5
"""
reading_time("string " * 300) => 1.5

"""
Given a string containing 50 words, returns a reading time of 0.5
"""
reading_time("string " * 100) => 0.5

"""
Given an empty string, returns an error
"""
reading_time("string " * 50) => "Cannot estimate time for an empty string."
```

## 4. Implement the Behaviour
