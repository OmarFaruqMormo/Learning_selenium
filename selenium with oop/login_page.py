from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self,driver):
        self.driver = driver
    # Navigate to login page
        self.driver.find_element(By.XPATH, "//a[@class='ico-login']").click()
    #Elements in Login page
        self.username_input = (By.XPATH, "//input[@id='Email']")
        self.password_input= (By.XPATH, "//input[@id='Password']")
        self.login_btn= (By.XPATH, "//button[text()='Log in']")


    def enter_username(self,username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_passward(self,password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_btn(self):
        self.driver.find_element(*self.login_btn).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_passward(password)
        self.click_btn()

