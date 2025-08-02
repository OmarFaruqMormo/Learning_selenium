import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.term_condition_checkbox = (By.ID, "termsofservice")
        self.checkout_button = (By.ID, "checkout")

        self.first_name_input = (By.ID, "BillingNewAddress_FirstName")
        self.last_name_input = (By.ID, "BillingNewAddress_LastName")
        self.country_dropdown = (By.ID, "BillingNewAddress_CountryId")
        self.state_dropdown = (By.ID, "BillingNewAddress_StateProvinceId")
        self.address1_input = (By.ID, "BillingNewAddress_Address1")
        self.continue_button = (By.XPATH, "//button[@onclick='Billing.save()']")

    def go_to_checkout_page(self):
        """Accept terms and go to checkout page"""
        term_box = self.driver.find_element(*self.term_condition_checkbox)
        if not term_box.is_selected():
            term_box.click()

        self.driver.find_element(*self.checkout_button).click()
        time.sleep(2)

        # Assertion to confirm we're on the checkout page
        assert "checkout" in self.driver.title.lower(), "Not the Checkout page"

    def fill_billing_address(self, first_name, last_name, country, state_value, address1):
        """Fill out billing address form"""
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

        country_element = self.driver.find_element(*self.country_dropdown)
        Select(country_element).select_by_visible_text(country)

        time.sleep(2)
        state_element = self.driver.find_element(*self.state_dropdown)
        Select(state_element).select_by_value(state_value)

        self.driver.find_element(*self.address1_input).send_keys(address1)

    def submit_billing_address(self):
        """Click on the continue button after filling billing info"""
        self.driver.find_element(*self.continue_button).click()

    def complete_billing_section(self, first_name, last_name, country, state_value, address1):
        """Combined method to fill and submit billing section"""
        self.fill_billing_address(first_name, last_name, country, state_value, address1)
        self.submit_billing_address()
