import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#step 1(Navigate to the website)

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://test.nop-station.store/")
time.sleep(2)

#step 3 (Login into the account)
#login with valid input

Login= driver.find_element(By.XPATH,"//a[@class='ico-login']")
Login.click()

username= driver.find_element(By.XPATH,"//input[@id='Username']")
username.send_keys("Mormo")
passward= driver.find_element(By.XPATH,"//input[@id='Password']")
passward.send_keys("Brain001")
loginbutton=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
loginbutton.click()

time.sleep(2)

#step 4 (search)

search=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
search.send_keys("Awesome")
searchbutton=driver.find_element(By.XPATH,"//button[@type='submit']")
searchbutton.click()
time.sleep(2)

#step 5 (add to cart)

add_to_cart_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Add to cart')]")
add_to_cart_buttons[0].click()      #clicking 1st add to curt button
time.sleep(1)
add_to_cart_buttons[2].click()      #clicking 3rd add to curt button
time.sleep(5)

shoppingcart=driver.find_element(By.CLASS_NAME,"ico-cart")
shoppingcart.click()

total_text= driver.find_element(By.CLASS_NAME,"value-summary").text
total_value = float(total_text.replace("$", "").replace(",", "").strip())

# Check if the total is at least $200
if total_value >= 200:
    print(" Total is greater than $200",)
else:
    print(" Total is less than $200")

# step 6
terms=driver.find_element(By.ID,"termsofservice")
terms.click()
driver.find_element(By.XPATH,"//button[@id='checkout']").click()
time.sleep(2)

#adding billing address
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_FirstName']").send_keys("M.A.Omar")
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_LastName']").send_keys("Faruq")
statedropdown =Select(driver.find_element(By.XPATH,"//select[@id='BillingNewAddress_StateProvinceId']"))
statedropdown.select_by_value("70")
driver.find_element(By.XPATH,"//input[@id='BillingNewAddress_Address1']").send_keys("Mirpur 2")
driver.find_element(By.XPATH,"//button[@onclick='Billing.save()']").click() #Billing address continue Button
time.sleep(3)
driver.find_element(By.XPATH,"//button[@onclick='Shipping.save()']").click() #Shipping address continue Button
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='button-1 shipping-method-next-step-button']").click() #Shipping method continue Button
time.sleep(2)
#driver.find_element(By.XPATH,"//label[normalize-space()='Credit Card']]").click() #Cradit card
driver.find_element(By.XPATH,"//button[@class='button-1 payment-method-next-step-button']").click() #Cradit card continue
time.sleep(2)
#cradit card info
card_type =Select(driver.find_element(By.XPATH,"//select[@id='CreditCardType']"))
card_type.select_by_value("visa")
driver.find_element(By.XPATH,"//input[@id='CardholderName']").send_keys("M.A.Omar Faruq")
driver.find_element(By.XPATH,"//input[@id='CardNumber']").send_keys("4111111111111111")
Expire_month =Select(driver.find_element(By.XPATH,"//select[@id='ExpireMonth']"))
Expire_month.select_by_visible_text("09")
Expire_year =Select(driver.find_element(By.XPATH,"//select[@id='ExpireYear']"))
Expire_year.select_by_visible_text("2030")
driver.find_element(By.XPATH,"//input[@id='CardCode']").send_keys("129")
driver.find_element(By.XPATH,"//button[@class='button-1 payment-info-next-step-button']").click() #card continue

#step 7
expected_name = "M.A.Omar Faruq"
name_element = driver.find_element(By.CLASS_NAME, "name")

actual_name = name_element.text.strip()

# Compare
if actual_name == expected_name:
    print("Name matches!")
else:
    print(f"Name does not match. Found: {actual_name}")

driver.find_element(By.XPATH,"//button[normalize-space()='Confirm']").click()

time.sleep(2)
driver.quit()