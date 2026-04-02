import pytest

from bank import value


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("hello", 0),
        ("Hello", 0),
        ("HELLO", 0),
        ("hey", 20),
        ("Hey", 20),
        ("HEY", 20),
        ("foo", 100),
        ("Foo", 100),
        ("FOO", 100),
    ],
)
def test_bank(input_value, expected):
    assert value(input_value) == expected
