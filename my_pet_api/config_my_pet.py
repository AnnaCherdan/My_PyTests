import pytest
import requests


@pytest.fixture
def key_param():
    res = requests.get(url='https://petfriends.skillfactory.ru/login',
                       data={'email': 'anchetest@mail.ru', 'password': 'ljkmvtyf'})
    return res
