import time


def test_pikabu_fox(driver_pikabu):
    driver_pikabu.find_element_by_name('username').send_keys('login')
    driver_pikabu.find_element_by_name('password').send_keys('password')
    driver_pikabu.find_element_by_xpath('/body/div[1]/div[1]/div[1]/aside/div[1]'
                                        '/div[1]/div/div[1]/div[2]/form/div[7]/button/span').click()
    time.sleep(3)
    driver_pikabu.close()
