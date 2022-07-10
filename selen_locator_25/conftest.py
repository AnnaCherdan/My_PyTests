import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture(autouse=True)
def driver(request):
    driver = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe')
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.find_element_by_xpath('//*[@id="email"]').send_keys('anchetest@mail.ru')
    driver.find_element_by_xpath('//*[@id="pass"]').send_keys('ljkmvtyf')
    driver.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    driver.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
    return driver
    # yield


# @pytest.fixture
# def get_chrome_options(driver):
#     chrome_options.binary_location = 'D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe'
#     cr_op = chrome_options()
#     cr_op.add_argument('chrome')
#     cr_op.add_argument('--window-size == 800, 600')
#     return cr_op


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe', options=chrome_options)
    return driver, chrome_options





