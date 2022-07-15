import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def chrome_options(chrome_options):
    chrome_options = Options()
    # chrome_options.set_headless(True)
    chrome_options.add_argument('--headless')
    return chrome_options


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


@pytest.fixture
def driver_friends(request):
    drifriend = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\Python\\chromedriver.exe')
    drifriend.get('https://petfriends.skillfactory.ru/login')
    drifriend.find_element_by_xpath('//input[@id="email"]').send_keys('anchetest@mail.ru')
    drifriend.find_element_by_xpath('//*[@id="pass"]').send_keys('ljkmvtyf')
    drifriend.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]').submit()
    drifriend.find_element_by_xpath('//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()
    return drifriend
