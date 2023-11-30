from lib.time_error import TimeError
import requests
from unittest.mock import Mock

def test_creates_class_object():
    timeerror = TimeError()
    assert isinstance(timeerror, TimeError)

def test_mocks_server_time_get():
    requster_mock = Mock(name = "requester")
    response_mock = Mock(name = "response")
    requster_mock.get.return_value = response_mock
    response_mock.json.return_value = {"abbreviation":"GMT",
                                        "client_ip":"158.41.48.3",
                                        "datetime":"2023-11-28T15:01:49.508080+00:00",
                                        "day_of_week":2,
                                        "day_of_year":332,
                                        "dst":False,
                                        "dst_from":None,
                                        "dst_offset":0,
                                        "dst_until":None,
                                        "raw_offset":0,
                                        "timezone":"Europe/London",
                                        "unixtime":1701183709,
                                        "utc_datetime":"2023-11-28T15:01:49.508080+00:00",
                                        "utc_offset":"+00:00",
                                        "week_number":48}
    timeerror = TimeError(requster_mock)
    assert timeerror.error() == 0.1