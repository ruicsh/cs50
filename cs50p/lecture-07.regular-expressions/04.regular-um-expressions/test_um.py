import pytest

from um import count


@pytest.mark.parametrize(
    "s,expected",
    [
        ("hello, um, world", 1),
        ("yummy", 0),
        ("um, hello, um, world", 2),
        ("um?", 1),
        ("Um, thanks for the album.", 1),
        ("Um, thanks, um...", 2),
    ],
)
def test_count(s, expected):
    assert count(s) == expected
