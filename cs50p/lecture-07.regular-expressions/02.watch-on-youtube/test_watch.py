import pytest

from watch import parse


@pytest.mark.parametrize(
    "html,expected",
    [
        (
            '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
        (
            '<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>',
            "https://youtu.be/xvFZjo5PgG0",
        ),
    ],
)
def test_parse(html, expected):
    assert parse(html) == expected
