import time

# class TestPF:


def test_login(driver_logo):
    time.sleep(5)

    search_input = driver_logo.find_element_by_id('email')
    search_input.send_keys('anchetest@mail.ru')

    search_input = driver_logo.find_element_by_id('pass')
    search_input.send_keys('ljkmvtyf')

    search_button = driver_logo.find_element_by_class_name('btn-success')
    search_button.submit()

    time.sleep(5)

    driver_logo.save_screenshot('result.png')


def test_path(driver):
    time.sleep(5)
    search_input = driver.find_element_by_xpath('//*[@id="email"]')
    search_input.send_keys('anchetest@mail.ru')

    search_input = driver.find_element_by_xpath('//*[@id="pass"]')
    search_input.send_keys('ljkmvtyf')

    time.sleep(5)

    search_button = driver.find_element_by_xpath('//body/div[1]/div[1]/form[1]/div[3]/button[1]')
    search_button.submit()


def test_path_drive(driver):
    time.sleep(3)
    assert driver.find_element_by_tag_name('h2').text == "AnnaCherdan"
    time.sleep(3)

    driver.close()



