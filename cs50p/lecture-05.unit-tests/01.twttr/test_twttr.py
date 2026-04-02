import pytest

from twttr import shorten


@pytest.mark.parametrize(
    "input_value, expected",
    [
        ("twitter", "twttr"),
        ("TWITTER", "twttr"),
        ("twttr", "twttr"),
        ("", ""),
        ("Twitter", "twttr"),
    ],
)
def test_twttr(input_value, expected):
    assert shorten(input_value) == expected
