from plates import is_valid


def test_plates_id_valid_true():
    cases = ["CS50", "CS", "CS150", "CS1250", "AAA222", "AAA200"]
    for case in cases:
        assert is_valid(case)


def test_plates_id_valid_false():
    cases = [
        "12",
        "1C",
        "C",
        "CS12345",
        "CS123456",
        "AAA22A",
        "AA22A2",
        "AAA022",
        "AABB!!",
    ]
    for case in cases:
        assert not is_valid(case)
