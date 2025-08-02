import time
from selenium import webdriver
from test_login import valid_login
from search_page import Search
from add_item import Add_item
from Cart_page import Cart_page
from Check_out_page import CheckOutPage

#Navigate to the website
driver=webdriver.Chrome()
driver.get("https://test.nop-station.store/en/")
driver.maximize_window()

#Navigate & login
valid_login(driver)
time.sleep(3)

#search
Search = Search(driver)
Search.search("Awesome")
time.sleep(3)

#add to cart
cart=Add_item(driver)
cart.add_item_to_cart(0)
time.sleep(2)
cart.add_item_to_cart(2)
time.sleep(5)

#go to cart Page and Check value
Cart_page(driver).check_value(200)
time.sleep(3)

#Check_out page
CheckOut= CheckOutPage(driver)
CheckOut.go_to_checkout_page()
CheckOut.complete_billing_section(
    first_name="M.A.Omar",
    last_name="Faruq",
    country="Bangladesh",
    state_value="70",
    address1="Mirpur 2"
)


driver.quit()
