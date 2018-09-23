from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://wikipedia.org")

#assert "" in driver.title
elem = driver.find_element_by_name("search")
elem.clear()
elem.send_keys("memes" +  Keys.RETURN)
assert "No results found." not in driver.page_source
print(driver.current_url)