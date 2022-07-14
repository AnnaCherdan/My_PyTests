import time


def test_pika_fox(drive_pikabu):
    drive_pikabu.get('https://pikabu.ru')
    time.sleep(3)
    drive_pikabu.find_element_by_name('username').send_keys('login')
    time.sleep(3)
    drive_pikabu.find_element_by_name('password').send_keys('password')
    time.sleep(3)
    drive_pikabu.find_element_by_xpath('//span[@class = "button__title"]').submit()
    time.sleep(3)
    assert drive_pikabu.find_element_by_xpath('//span[@class = "auth__error"]').is_displayed(), 'AHTUNG'
    drive_pikabu.close()
