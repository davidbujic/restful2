from test import comment_get, comment_post


def test_comment_get():
    assert comment_get() == 200


def test_comment_post():
    assert comment_post() == 201
