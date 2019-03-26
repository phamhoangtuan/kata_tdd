from unittest.mock import MagicMock
from Hello.code import Hello


def test_can_say_hello():
    obj = Hello()
    assert obj.say_hello() == 'Hello World!'


def test_can_say_other_word():
    other_obj = MagicMock()
    other_obj.word = 'Hello from MagicMock'
    obj = Hello(other_obj)
    assert obj.say_hello() == 'Hello from MagicMock'
