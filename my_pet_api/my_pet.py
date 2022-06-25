import requests
import json
from config_my_pet import log_key_param


def test_logo():
    logo_key = requests.get(url='https://petfriends.skillfactory.ru/login',
                            data={"email": "anchetest@mail.ru", "password": "ljkmvtyf"})
    assert logo_key.status_code == 200


def test_apikey(log_key_param):
    header = {"accept": "application/json", "email": "anchetest@mail.ru", "password": "ljkmvtyf"}
    apikey = requests.get(url='https://petfriends.skillfactory.ru/api/key',
                          headers=header)
    print(apikey.text)
    assert apikey.status_code == 200
    assert list(json.loads(apikey.text))
    print(list(json.loads(apikey.text)))
