import pytest
import requests


@pytest.fixture
def log_key_param():
    header = {"accept": "application/json", "email": "anchetest@mail.ru", "password": "ljkmvtyf"}
    logo_key = requests.post(url='https://petfriends.skillfactory.ru/login',
                             data=header)
    return logo_key

