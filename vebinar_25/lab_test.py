import time


def test_1(driver_friends):
    driver_friends.implicitly_wait(10)
    # assert driver_pikabu.find_element_by_xpath('//*[@id="adfox_156570562144159249"]/div[1]/a[1]')\
    #     .is_displayed(), "AHTUNG VISIBLE"
    driver_friends.implicitly_wait(10)
    # assert driver_friends.find_element_by_xpath('//body/div[1]/div[1]/h1[1]').is_displayed, 'Все сломалось!'
    driver_friends.close()
