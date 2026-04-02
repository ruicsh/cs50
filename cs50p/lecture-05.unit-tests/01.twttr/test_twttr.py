from twttr import shorten


def test_twttr():
    cases = [
        ["twitter", "twttr"],
        ["TWITTER", "twttr"],
        ["twttr", "twttr"],
        ["", ""],
        ["Twitter", "twttr"],
    ]
    for case in cases:
        input, expected = case
        assert shorten(input) == expected
