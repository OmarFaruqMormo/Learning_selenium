from selenium.webdriver.common.by import By

class Cart_page:
    def __init__(self,driver):
        self.driver=driver
        self.shopping_cart_button = driver.find_element(By.CLASS_NAME, "ico-cart").click()
        self.total_text = driver.find_element(By.CLASS_NAME, "value-summary").text

    def check_value(self,min_value):

        total_value = float(self.total_text.replace("$", "").replace(",", "").strip())
        print("Total value is: ",total_value)

        assert total_value>= min_value, f"Value is under the minimum: {min_value}"