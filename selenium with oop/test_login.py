import time
from login_page import Loginpage

def valid_login(driver):

    loginpage = Loginpage(driver)
    loginpage.login("omarfaruq.reza02@gmail.com","Brain001")

    print("The title is: ", driver.title)
    assert "Your store" in driver.title, "login Failed"

def invalid_login(driver,username,password):

    loginpage = Loginpage(driver)
    loginpage.login(username,password)

    print("The title is: ", driver.title)
    assert "Your store" in driver.title, "login Failed"

