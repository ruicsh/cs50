import pytest

from fuel import convert, gauge


@pytest.mark.parametrize(
    "input_value, expected", [["1/4", 25], ["1/2", 50], ["3/4", 75]]
)
def test_convert_ok(input_value, expected):
    assert convert(input_value) == expected


@pytest.mark.parametrize("input_value", ["4/1", "2/1", "4/3"])
def test_convert_not_fractions(input_value):
    with pytest.raises(ValueError):
        convert(input_value)


@pytest.mark.parametrize("input_value", ["cat", "dog", "foo", "cat/dog"])
def test_convert_strings(input_value):
    with pytest.raises(ValueError):
        convert(input_value)


def test_convert_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


@pytest.mark.parametrize(
    "input_value, expected",
    [
        (0, "E"),
        (1, "E"),
        (99, "F"),
        (100, "F"),
        (30, "30%"),
        (50, "50%"),
        (80, "80%"),
    ],
)
def test_gauge(input_value, expected):
    assert gauge(input_value) == expected
