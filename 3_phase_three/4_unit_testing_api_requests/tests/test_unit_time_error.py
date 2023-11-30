from lib.time_error import TimeError
import requests
from unittest.mock import Mock

def test_mocks_server_time_get():
    requester_mock = Mock()
    response_mock = Mock()
    timer_mock = Mock()

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime":1701183709}

    timer_mock.time.return_value = 1701183709.5
    time_error = TimeError(requester_mock, timer_mock)

    assert isinstance(time_error, TimeError)
    assert time_error.error() == -0.5
