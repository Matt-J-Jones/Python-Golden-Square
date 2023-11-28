from lib.secret_diary import SecretDiary
from unittest.mock import Mock

fake_diary = Mock()

def test_creates_object():
    secretdiary = SecretDiary(fake_diary)
    assert isinstance(secretdiary, SecretDiary)

def test_locks_unlocks_diary():
    secretdiary = SecretDiary(fake_diary)
    assert secretdiary.locked is True
    secretdiary.unlock()
    assert secretdiary.locked is False
    secretdiary.lock()
    assert secretdiary.locked is True

def test_adds_mocked_diary_returns_locked():
    fake_diary.read.return_value = "Hello, World"
    secretdiary = SecretDiary(fake_diary)
    assert secretdiary.read() == "Go, away!"

def test_adds_mocked_diary_returns_text():
    fake_diary.read.return_value = "Hello, World"
    secretdiary = SecretDiary(fake_diary)
    secretdiary.unlock()
    assert secretdiary.read() == "Hello, World"