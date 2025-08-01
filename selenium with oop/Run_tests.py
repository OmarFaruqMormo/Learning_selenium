import time
from selenium import webdriver
from test_login import valid_login
from search_page import Search
from add_item import Add_item

driver=webdriver.Chrome()

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


driver.quit()
