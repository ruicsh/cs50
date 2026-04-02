import pytest

from fuel import convert, gauge


def test_convert_ok():
    cases = [["1/4", 25], ["1/2", 50], ["3/4", 75]]
    for case in cases:
        input, expected = case
        assert convert(input) == expected


def test_convert_not_fractions():
    inputs = ["4/1", "2/1", "4/3"]
    for input in inputs:
        with pytest.raises(ValueError):
            convert(input)


def test_convert_strings():
    inputs = ["cat", "dog", "foo", "cat/dog"]
    for input in inputs:
        with pytest.raises(ValueError):
            convert(input)


def test_convert_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge():
    cases = [
        [0, "E"],
        [1, "E"],
        [99, "F"],
        [100, "F"],
        [30, "30%"],
        [50, "50%"],
        [80, "80%"],
    ]
    for case in cases:
        input, expected = case
        assert gauge(input) == expected
