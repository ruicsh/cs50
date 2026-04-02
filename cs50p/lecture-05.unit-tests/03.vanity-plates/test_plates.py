import pytest

from plates import is_valid


@pytest.mark.parametrize(
    "input_value", ["CS50", "CS", "CS150", "CS1250", "AAA222", "AAA200"]
)
def test_plates_id_valid_true(input_value):
    assert is_valid(input_value)


@pytest.mark.parametrize(
    "input_value",
    [
        "12",
        "1C",
        "C",
        "CS12345",
        "CS123456",
        "AAA22A",
        "AA22A2",
        "AAA022",
        "AABB!!",
    ],
)
def test_plates_id_valid_false(input_value):
    assert not is_valid(input_value)
