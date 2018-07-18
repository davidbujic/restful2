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


# api/Hello GET
print "Hello World:"
r = requests.get('http://0.0.0.0:8090/api/Hello')
if r.status_code == 200:
    print "OK"
else:
    print r.status_code

# api/Category GET
print "Category GET:"
r = requests.get('http://0.0.0.0:8090/api/Category')
if r.status_code == 200:
    print "OK"
else:
    print r.status_code

# api/Category POST
print "Category POST:"
payload = {'name': 'example'}
r = requests.post('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
result = json.loads(r.text.decode('utf-8'))
id = result["data"]["id"]
if r.status_code == 201:
    print "OK"
else:
    print r.status_code

# api/Category PUT
print "Category PUT:"
payload = {'id': id, 'name': 'reserved'}
r = requests.put('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
if r.status_code == 204:
    print "OK"
else:
    print r.status_code

# api/Comment POST
print "Comment POST:"
payload = {'category_id': id, 'comment': 'COMMENT'}
r = requests.post('http://0.0.0.0:8090/api/Comment', data=json.dumps(payload))
if r.status_code == 201:
    print "OK"
else:
    print r.status_code

# api/Comment GET
print "Comment GET:"
r = requests.get('http://0.0.0.0:8090/api/Comment')
if r.status_code == 200:
    print "OK"
else:
    print r.status_code

# api/Category DELETE
print "Category DELETE:"
payload = {'id': id, 'name': 'reserved'}
r = requests.delete('http://0.0.0.0:8090/api/Category', data=json.dumps(payload))
if r.status_code == 204:
    print "OK"
else:
    print r.status_code
