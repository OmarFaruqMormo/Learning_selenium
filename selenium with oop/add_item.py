from selenium.webdriver.common.by import By

class Add_item:
    def __init__(self,driver):
        self.driver=driver

        self.add_to_cart_buttons=driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
        self.shopping_cart_button = driver.find_element(By.CLASS_NAME,"ico-cart")


    def add_item_to_cart(self,index):
        self.add_to_cart_buttons[index].click()

    def go_to_cart(self):
        self.shopping_cart_button.click()
