from selenium import webdriver

import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:/Users/jutsi/Documents/chromedriver.exe")


def retrieve_email():
    driver.get("http://localhost/phpmyadmin/db_structure.php?server=1&db=apm72")
    time.sleep(1)
    elem = driver.find_elements_by_class_name("hover_show_full")
    time.sleep(1)
    for x in range(3, len(elem)):
        elem[x].click()
        time.sleep(1)
        tabs = driver.find_elements_by_class_name("tab")
        tabs[4].click()
        time.sleep(1)

        select = Select(driver.find_element_by_id('plugins'))
        select.select_by_value("csv")
        time.sleep(1)
        go_button = driver.find_element_by_id("buttonGo").click()

    elem[3].click()
    time.sleep(5)
    tabs = driver.find_elements_by_class_name("tab")
    tabs[4].click()
    time.sleep(5)
    select = Select(driver.find_element_by_id('plugins'))
    select.select_by_value("csv")
    go_button = driver.find_element_by_id("buttonGo").click()
    elem[4].click()

    # assert "No results found." not in driver.page_source
    # print(elem.get_attribute("value"))
    # return elem.get_attribute("value")
    # driver.close()
