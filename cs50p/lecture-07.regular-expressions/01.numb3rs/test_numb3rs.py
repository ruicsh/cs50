import pytest

from numb3rs import validate


@pytest.mark.parametrize(
    "ip,expected",
    [
        ("0.0.0.0", True),
        ("127.0.0.1", True),
        ("255.255.255.0", True),
        ("275.255.255.0", False),
        ("cat", False),
        ("cat.dog.duck.fish", False),
    ],
)
def test_validate(ip, expected):
    assert validate(ip) == expected
