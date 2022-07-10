import pytest
from selenium import webdriver


@pytest.fixture
def get_webdriver(request):
    driver = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\webdrivers\\chromedriver.exe')
    return driver
