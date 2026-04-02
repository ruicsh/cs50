from bank import value


def test_bank():
    cases = [
        ["hello", 0],
        ["Hello", 0],
        ["HELLO", 0],
        ["hey", 20],
        ["Hey", 20],
        ["HEY", 20],
        ["foo", 100],
        ["Foo", 100],
        ["FOO", 100],
    ]
    for case in cases:
        input, expected = case
        assert value(input) == expected
