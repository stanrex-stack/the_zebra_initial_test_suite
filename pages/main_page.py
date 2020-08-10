from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    CAR_INSURANCE = (By.CSS_SELECTOR, '.hero-homepage [data-cy="auto-funnel-selection"]')
    ZIP_INPUT_FIELD = (By.CSS_SELECTOR, '.hero-homepage .zipcode-text-input')
    START_BUTTON = (By.CSS_SELECTOR, '.hero-homepage .form-inline-submit-button')
    INSTAGRAM_LINK = (By.CSS_SELECTOR, 'a[href*="instagram"]')
    # Zip Error
    ZIP_ERROR = (By.CSS_SELECTOR, '.hero-homepage .form-control-feedback')
    ZIP_ERROR_TEXT = (By.CSS_SELECTOR, '.hero-homepage .form-control-feedback p')

    def main_open(self):
        self.open_page()

    def click_car_insurance(self):
        self.wait_for_element_to_be_clickable_click(*self.CAR_INSURANCE)

    def click_start(self):
        self.wait_for_element_to_be_clickable_click(*self.START_BUTTON)

    def click_instagram_link(self):
        self.wait_for_element_to_be_clickable_click(*self.INSTAGRAM_LINK)

    def input_zip(self, zip: str):
        self.wait_for_element_to_appear(*self.ZIP_INPUT_FIELD)
        self.input(zip, *self.ZIP_INPUT_FIELD)

    def verify_zip_error_present(self):
        self.wait_for_element_to_appear(*self.ZIP_ERROR)

    def verify_zip_error_text(self, text):
        self.verify_element_text(text, *self.ZIP_ERROR_TEXT)
