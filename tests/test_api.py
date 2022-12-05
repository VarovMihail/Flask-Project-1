import requests
from tests.config import API_URL


def test_root():
    response = requests.get(API_URL)
    # print(f'{response.status_code = }')
    assert response.status_code == 404


def test_hello_word():
    response = requests.get(f'{API_URL}/hw')
    assert response.status_code == 200
    assert response.text == 'Hello Word!'


def test_get_user_by_id(create_user):
    user = create_user
    print(f'{user = }')
    print(f'{user["id"] = }')
    print(f'{API_URL}/users/{user["id"]}')
    response = requests.get(f'{API_URL}/users/{user["id"]}')
    print(f'{response = }')
    print(f'{response.json = }')
    response_json = response.json()
    print(f'{response_json = }')
    assert response.status_code == 200
    assert user['email'] == response_json['email']


def test_create_user():
    response = requests.post(f'{API_URL}/users', json={'email': 'new@mail.ru', 'password': 123})
    response_json = response.json()
    print(response_json)
    assert response.status_code == 200
    assert response_json['email'] == 'new@mail.ru'


def test_delete_user(create_user):
    user = create_user
    response = requests.delete(f'{API_URL}/users/{user["id"]}')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'deleted'


def test_get_adv_by_id(create_advertisement):
    adv = create_advertisement
    print(f'{adv = }')
    response = requests.get(f'{API_URL}/advertisements/{adv["id"]}')
    response_json = response.json()
    print(response_json)
    assert response.status_code == 200
    assert adv['id'] == response_json['id']


def test_delete_adv(create_advertisement):
    adv = create_advertisement
    response = requests.delete(f'{API_URL}/advertisements/{adv["id"]}')
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['status'] == 'deleted'


def test_create_adv(create_user):
    data = {
        'title': 'some_title',
        'description': 'some_description',
        'user_id': create_user['id'],
    }
    response = requests.post(f'{API_URL}/advertisements/', json=data)
    response_json = response.json()
    assert response.status_code == 200
    assert response_json['title'] == data['title']
