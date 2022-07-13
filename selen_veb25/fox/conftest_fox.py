import pytest
from selenium import webdriver


@pytest.fixture
def driver_pikabu(request):
    drivepik = webdriver.Firefox("/usr/local/bin/geckodriver")
    drivepik.get('https://pikabu.ru')
    return drivepik
