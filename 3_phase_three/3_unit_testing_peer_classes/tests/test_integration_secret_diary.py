from lib.diary import Diary
from lib.secret_diary import SecretDiary

diary = Diary("Hello, World")


def test_locks_unlocks_diary():
    secretdiary = SecretDiary(diary)
    assert secretdiary.locked is True
    secretdiary.unlock()
    assert secretdiary.locked is False
    secretdiary.lock()
    assert secretdiary.locked is True

def test_adds_diary_returns_locked():
    secretdiary = SecretDiary(diary)
    assert secretdiary.read() == "Go, away!"

def test_adds_diary_returns_text():
    secretdiary = SecretDiary(diary)
    secretdiary.unlock()
    assert secretdiary.read() == "Hello, World"