from selenium import webdriver
driver = webdriver.Chrome("C:/Users/jutsi/Documents/chromedriver.exe")
import random

def create_account(mail):
    driver.get("https://www.instagram.com/")
    # insert_mail(mail)
    # insert_full_name()
    # insert_username()
    # insert_password()




# def insert_full_name():
#     first_name_field = driver.find_element_by_name("fullName")
#     first_name_field.send_keys("Temporary Name")
#     print ("full name: Temporary Name")
#
# def insert_mail(mail):
#     email_field = driver.find_element_by_name("emailOrPhone")
#     email_field.send_keys(mail)
#     print("email: "+mail)
#
# def insert_username():
#     username_field = driver.find_element_by_name("username")
#     username = "memescape" + random.randint(0, 200)
#     username_field.send_keys(username)
#     print("username:" + username)
#
# def insert_password():
#     password_field = driver.find_element_by_name("password")
#     password_field.send_keys("124587963")
#     print("pass:" + 124587963)
