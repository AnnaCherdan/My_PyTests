import time


def test_login(driver, get_chrome_options):
    driver.get('https://petfriends.skillfactory.ru/login')

    time.sleep(5)

    search_input = driver.find_element_by_id('email')
    search_input.send_keys('anchetest@mail.ru')

    search_input = driver.find_element_by_id('pass')
    search_input.send_keys('ljkmvtyf')

    # search_button = driver.find_element_by_test('Войти')
    # search_button.submit()


    time.sleep(5)








