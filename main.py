import requests
import json

'''
I used https://fakerestapi.azurewebsites.net for testing.
'''


def get_authors():
    resp = requests.get('https://fakerestapi.azurewebsites.net/api/Authors')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    for todo_item in resp.json():
        print(type(todo_item))
        print('{} {}'.format(todo_item['ID'], todo_item['FirstName']))


def get_author_id(id):
    param = {'id': id}
    resp = requests.get(
        'https://fakerestapi.azurewebsites.net/api/Authors', params=param)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /api/author {}'.format(resp.status_code))
    print('{} {}'.format(resp.json()['LastName'], resp.json()['FirstName']))


def post_author(auther_dic):
    resp = requests.post(
        'https://fakerestapi.azurewebsites.net/api/Authors',
        data=json.dumps(auther_dic),
        headers={'Content-Type': 'application/json'})
    print(resp.status_code)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('POST /api/author {}'.format(resp.status_code))
    print('Saved Author.ID: {}'.format(resp.json()['ID']))


author_dic = {
    "ID": 122,
    "IDBook": 2,
    "FirstName": "sample string 3",
    "LastName": "sample string 4"
}

post_author(author_dic)
