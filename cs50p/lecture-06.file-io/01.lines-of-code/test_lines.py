import pytest

from lines import get_file_extension, is_line_of_code


@pytest.mark.parametrize(
    "filename, expected", [("", ""), ("foobar", ""), ("foobar.py", ".py")]
)
def test_get_file_extension(filename, expected):
    assert get_file_extension(filename) == expected


@pytest.mark.parametrize(
    "line,expected",
    [
        ("# comment", False),
        ("", False),
        ("       ", False),
        ("print(f)", True),
        ('" docstring', True),
    ],
)
def test_is_line_of_code(line, expected):
    assert is_line_of_code(line) == expected
