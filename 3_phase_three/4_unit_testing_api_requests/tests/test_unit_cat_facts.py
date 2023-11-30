from lib.cat_facts import CatFacts
from unittest.mock import Mock

def test_mocks_api_return():
    requester_mock = Mock()
    response_mock = Mock()

    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact":"Cats' hearing is much more sensitive than humans and dogs.","length":58}

    cat_fact = CatFacts(requester_mock)

    assert isinstance(cat_fact, CatFacts)
    assert cat_fact.provide() == "Cat fact: Cats' hearing is much more sensitive than humans and dogs."
