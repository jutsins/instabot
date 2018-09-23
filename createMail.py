from selenium import webdriver
driver = webdriver.Chrome()


def retrieve_email():
    driver.get("https://10minutemail.net/?lang=nl")
    elem = driver.find_element_by_class_name("mailtext")
    if elem.get_attribute("value") == "":
        print (":(")

    assert "No results found." not in driver.page_source
    print(elem.get_attribute("value"))
    return elem.get_attribute("value")
    driver.close()
