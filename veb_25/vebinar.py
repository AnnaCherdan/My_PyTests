import time
import pytest
from selenium import webdriver


def test_1():
    driver = webdriver.Chrome('D:\\AllDoc\\AnnCherdan\\webdrivers\\chromedriver.exe')
    driver.get('https://www.labirint.ru/')
