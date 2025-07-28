import time

from test_login import valid_login
from search_page import Search


driver = valid_login()

time.sleep(3)
Search(driver).search("Awesome")
time.sleep(3)

driver.quit()
