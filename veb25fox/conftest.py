import pytest
from selenium import webdriver


@pytest.fixture
def drive_pikabu(request):
    drive = webdriver.Firefox()
    drive.get('https://pikabu.ru')
    return drive
