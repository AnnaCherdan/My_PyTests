import pytest
from selenium import webdriver


@pytest.fixture
def driver_pikabu(request):
    driver_pik = webdriver.Chrome("/usr/local/bin/chromedriver")
    return driver_pik
