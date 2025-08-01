import time
from login_page import Loginpage

def valid_login(driver):

    driver.get("https://test.nop-station.store/en/")
    driver.maximize_window()

    loginpage = Loginpage(driver)
    loginpage.login("omarfaruq.reza02@gmail.com","Brain001")
    time.sleep(3)

    print("The title is: ", driver.title)
    assert "Your store" in driver.title, "login Failed"


