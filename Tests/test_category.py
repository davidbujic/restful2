from test import category_get, category_post, category_put, category_delete


def test_category_get():
    assert category_get() == 200


def test_category_post():
    assert category_post() == 201


def test_category_put():
    assert category_put() == 204


def test_category_delete():
    assert category_delete() == 204
