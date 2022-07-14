import time


def test_1(driver_friends):
    time.sleep(3)
    # assert driver_friends.find_element_by_xpath('//*[@id="pass"]').send_keys('gjhfjhjh')
    # assert driver_friends.find_element_by_xpath('//body/div[1]/div[1]/h1[1]').is_displayed, 'Все сломалось!'
    # time.sleep(3)
    driver_friends.close()
