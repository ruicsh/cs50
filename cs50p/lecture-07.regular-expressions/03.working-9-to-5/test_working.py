import pytest

from working import convert, convert_time


@pytest.mark.parametrize(
    "s,expected",
    [
        ("9:00 AM to 5:00 PM", "09:00 to 17:00"),
        ("9 AM to 5 PM", "09:00 to 17:00"),
        ("9:00 AM to 5 PM", "09:00 to 17:00"),
        ("9 AM to 5:00 PM", "09:00 to 17:00"),
        ("5:00 PM to 9:00 AM", "17:00 to 09:00"),
    ],
)
def test_convert(s, expected):
    assert convert(s) == expected


@pytest.mark.parametrize(
    "time,expected",
    [
        ("9:00 AM", "09:00"),
        ("9 AM", "09:00"),
        ("5:00 PM", "17:00"),
        ("5 PM", "17:00"),
    ],
)
def test_convert_time(time, expected):
    assert convert_time(time) == expected


@pytest.mark.parametrize("s", ["12:60 AM", "13:00 PM"])
def test_convert_time_raises(s):
    with pytest.raises(ValueError):
        assert convert_time(s)
