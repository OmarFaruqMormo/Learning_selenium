import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from login_page import loginpage

def valid_login():
    driver= webdriver.Chrome()
    driver.get("https://test.nop-station.store/en/")
    driver.maximize_window()

    driver.find_element(By.XPATH,"//a[@class='ico-login']").click()

    lpage = loginpage(driver)
    lpage.login("omarfaruq.reza02@gmail.com","Brain001")


    time.sleep(3)
    print("The title is", driver.title)
    return driver

