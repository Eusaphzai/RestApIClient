import requests
import json

def get_authors():
    resp=requests.get('https://fakerestapi.azurewebsites.net/api/Authors')
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    for todo_item in resp.json():
        print(type(todo_item))
        print('{} {}'.format(todo_item['ID'], todo_item['FirstName']))

def get_author_id(id):
    param={'id':id}
    resp=requests.get('https://fakerestapi.azurewebsites.net/api/Authors'
    ,params=param)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /tasks/ {}'.format(resp.status_code))
    print('{} {}'.format(resp.json()['LastName'], resp.json()['FirstName']))

