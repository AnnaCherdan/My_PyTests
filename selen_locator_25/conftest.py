import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe')
    return driver


@pytest.fixture
def get_chrome_options(driver):
    chrome_options.binary_location = 'D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe'
    cr_op = chrome_options()
    cr_op.add_argument('chrome')
    cr_op.add_argument('--window-size == 800, 600')
    return cr_op


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe', options=chrome_options)
    return driver, chrome_options





