import requests
import json


def hello_get():
    r = requests.get('http://0.0.0.0:8090/api/Hello')
    return r.status_code


def category_get():
    r = requests.get('http://0.0.0.0:8090/api/Category')
    return r.status_code


def category_post():
    payload = {'name': 'example'}
    r = requests.post('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
    result = json.loads(r.text.decode('utf-8'))
    id = result["data"]["id"]
    payload = {'id': id, 'name': 'example'}
    rdel = requests.delete('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
    return r.status_code


def category_put():
    payload = {'id': 2, 'name': 'example'}
    r = requests.put('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
    payload = {'id': 2, 'name': 'reserved'}
    r = requests.put('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
    return r.status_code


def category_delete():
    payload = {'name': 'example'}
    r = requests.post('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
    result = json.loads(r.text.decode('utf-8'))
    id = result["data"]["id"]
    payload = {'id': id, 'name': 'example'}
    rdel = requests.delete('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
    return rdel.status_code


def comment_post():
    payload = {'category_id': 2, 'comment': 'COMMENT'}
    r = requests.post('http://0.0.0.0:8090/api/Comment', data=json.dumps(payload))
    return r.status_code


def comment_get():
    r = requests.get('http://0.0.0.0:8090/api/Comment')
    return r.status_code
