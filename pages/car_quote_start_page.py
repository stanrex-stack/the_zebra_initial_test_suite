from pages.base_page import Page
from selenium.webdriver.common.by import By


class CarStartPage(Page):
    CONTINUE_BTN = (By.CSS_SELECTOR, "button[name='continue']")
    # Question 1
    HAVE_INSURANCE_YES = (By.CSS_SELECTOR, 'label[for="currently_insured-1start"]')
    HAVE_INSURANCE_NO = (By.CSS_SELECTOR, 'label[for="currently_insured-0start"]')
    # Question 2
    OWN_HOME_ANSWER = (By.CSS_SELECTOR, 'label[for="residence_ownership-{SUBSTRING_OPTION}start"]')
    SECOND_QUESTION_TEXT_LOCATOR = (By.CSS_SELECTOR, '#residence_ownershipstart h3')
    SECOND_QUESTION_TIP_TEXT_LOCATOR = (By.CSS_SELECTOR, '#residence_ownershipstart p')
    # Question 3
    THIRD_QUESTION_TEXT_LOCATOR = (By.CSS_SELECTOR, '#user_intentstart h3')
    WHY_SHOPPING_ANSWER = (By.XPATH, "//label[./input[@name='user_intent-0start']]")
    # PII input fields
    GARAGING_ADDRESS_INPUT_FIELD = (By.ID, 'garaging_addressInput')
    GARAGING_ADDRESS_FIRST_RESULT = (By.CSS_SELECTOR, 'div.pac-container div:nth-of-type(1)')
    FIRST_NAME_INPUT_FIELD = (By.ID, 'first_namestart')
    LAST_NAME_INPUT_FIELD = (By.ID, 'last_namestart')
    BIRTH_DATE_INPUT_FIELD = (By.ID, 'date_of_birthstart')

    def _get_own_home_answer_locator(self, option):
        return [self.OWN_HOME_ANSWER[0], self.OWN_HOME_ANSWER[1].replace('{SUBSTRING_OPTION}', option)]

    def _get_why_shopping_answer_locator(self, option):
        return [self.WHY_SHOPPING_ANSWER[0], self.WHY_SHOPPING_ANSWER[1].replace('{SUBSTRING_OPTION}', option)]

    def select_if_have_insurance(self, answer: str):
        answer = answer.lower()
        if answer == "yes":
            self.wait_for_element_to_be_clickable_click(*self.HAVE_INSURANCE_YES)
        elif answer == "no":
            self.wait_for_element_to_be_clickable_click(*self.HAVE_INSURANCE_NO)

    def select_if_own_home(self, option: str):
        locator = self._get_own_home_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def select_why_shopping(self, option: str):
        locator = self._get_why_shopping_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def click_continue(self):
        e = self.wait_for_element_to_appear(*self.CONTINUE_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        self.wait_for_element_to_be_clickable_click(*self.CONTINUE_BTN)

    def enter_address(self, address):
        self.wait_for_element_to_appear(*self.GARAGING_ADDRESS_INPUT_FIELD)
        self.input(address, *self.GARAGING_ADDRESS_INPUT_FIELD)
        self.wait_for_element_to_be_clickable_click(*self.GARAGING_ADDRESS_FIRST_RESULT)

    def enter_first_name(self, first):
        self.input(first, *self.FIRST_NAME_INPUT_FIELD)

    def enter_last_name(self, last):
        self.input(last, *self.LAST_NAME_INPUT_FIELD)

    def enter_dob(self, dob):
        self.input(dob, *self.BIRTH_DATE_INPUT_FIELD)
