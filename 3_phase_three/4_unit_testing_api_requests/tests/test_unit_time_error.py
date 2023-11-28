from lib.time_error import TimeError

def test_creates_class_object():
    timeerror = TimeError()
    assert isinstance(timeerror, TimeError)