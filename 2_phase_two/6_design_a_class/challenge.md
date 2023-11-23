# Music Library Class Design Recipe

## 1. Describe the Problem
```
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
```

## 2. Design the Class Interface

```python
# EXAMPLE

class MusicLibrary:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        # task_list = []
        pass # No code here yet

    def add(self, track)
        # Paramerer: track - string  - adds track to list
        pass # No code here yet
    
    def print_list(self)
        # prints list of tracks
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Adds track to tracklist
"""
music_library = MusicLibrary()
music_library.add("Echo Chamber Experiment", "Stardust Serenade")
todo.print_list() # => "Echo Chamber Experiment - Stardust Serenade"

"""
Adds tracks to tracklist
"""
music_library = MusicLibrary()
music_library.add("Echo Chamber Experiment", "Stardust Serenade")
music_library.add("Celestial Pulse", "Echoes of Infinity")
music_library.add("Electric Echoes", "Eclipsed Dreams")
music_library.add("Crimson Horizon", "Aurora Borealis Blues")
music_library.add("Crimson Horizon", "Nebula Waltz")
todo.print_list() # => "Echo Chamber Experiment - Stardust Serenade, Celestial Pulse - Echoes of Infinity, 
# Electric Echoes - Eclipsed Dreams, Crimson Horizon - Crimson Horizon, Crimson Horizon - Nebula Waltz"

"""
Adds empty track to library, raises error
"""
music_library = MusicLibrary()
music_library.add(None, None) # raises an error with the message "No track to add"

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
