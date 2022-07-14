import pytest
from selenium import webdriver


@pytest.fixture
def driver_pikabu(request):
    dripik = webdriver.Chrome("/usr/local/bin/chromedriver")
    dripik.get('https://pikabu.ru')
    return dripik
