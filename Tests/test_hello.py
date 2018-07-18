from test import hello_get


def test_hello_get():
    assert hello_get() == 200
