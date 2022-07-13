import pytest
from selenium import webdriver


@pytest.fixture
def driver_labirint(request):
    driver_lab = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe')
    driver_lab.get('https://www.labirint.ru/')
    return driver_lab


@pytest.fixture(autouse=True)
def driver_pikabu(request):
    driver_pik = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe')
    driver_pik.get('https://pikabu.ru/')
    return driver_pik
