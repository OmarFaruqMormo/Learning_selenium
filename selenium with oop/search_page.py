from selenium.webdriver.common.by import By

class Search():
    def __init__(self,driver):
        self.driver = driver

        self.searchbox= (By.XPATH,"//input[@id='small-searchterms']")
        self.searchbtn= (By.XPATH,"//button[@type='submit']")

    def search(self,title):
        self.driver.find_element(*self.searchbox).send_keys(title)
        self.driver.find_element(*self.searchbtn).click()