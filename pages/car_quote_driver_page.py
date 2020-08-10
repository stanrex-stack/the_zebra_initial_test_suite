from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CarDriverOnePage(Page):

    GENDER_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="gender-0-0"]')
    # TODO {SUBSTRING_OPTION}
    GENDER_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="gender-{SUBSTRING_OPTION}-0"]')

    MARITAL_QUESTION_RADIO_ONER = (By.CSS_SELECTOR, 'label[for="marital_status-0-0"]')
    # TODO {SUBSTRING_OPTION}
    MARITAL_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="marital_status-1-0"]')
    MARITAL_QUESTION_RADIO_THREE = (By.CSS_SELECTOR, 'label[for="marital_status-2-0"]')
    MARITAL_QUESTION_RADIO_FOUR = (By.CSS_SELECTOR, 'label[for="marital_status-3-0"]')

    CREDIT_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="credit_score-0-0"]')
    # TODO {SUBSTRING_OPTION}
    CREDIT_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="credit_score-1-0"]')
    CREDIT_QUESTION_RADIO_THREE = (By.CSS_SELECTOR, 'label[for="credit_score-2-0"]')
    CREDIT_QUESTION_RADIO_FOUR = (By.CSS_SELECTOR, 'label[for="credit_score-4-0"]')

    EDUCATION_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="education-4-0"]')
    # TODO {SUBSTRING_OPTION}
    EDUCATION_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="education-3-0"]')
    EDUCATION_QUESTION_RADIO_THREE = (By.CSS_SELECTOR, 'label[for="education-2-0"]')
    EDUCATION_QUESTION_RADIO_FOUR = (By.CSS_SELECTOR, 'label[for="education-1-0"]')
    EDUCATION_QUESTION_RADIO_FIVE = (By.CSS_SELECTOR, 'label[for="education-0-0"]')

    INSURED_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="insured_length-3-0"]')
    # TODO {SUBSTRING_OPTION}
    INSURED_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="insured_length-2-0"]')
    INSURED_QUESTION_RADIO_THREE = (By.CSS_SELECTOR, 'label[for="insured_length-1-0"]')
    INSURED_QUESTION_RADIO_FOUR = (By.CSS_SELECTOR, 'label[for="insured_length-0-0"]')

    CURRENT_PROVIDER_FIELD = (By.ID, "current_carrierCurrent_carrierInput-0")
        # (By.CSS_SELECTOR, 'label[for="current_carrierCurrent_carrierInput-0"]')
    CURRENT_PROVIDER_FIRST_SELECT = (By.CSS_SELECTOR, '#current_carrier-0 div.item:nth-of-type(1)')

    VIOLATIONS_QUESTION_FIRST_ANSWER = (By.CSS_SELECTOR, 'label[for="violations-1-0"]')
    # TODO {SUBSTRING_OPTION}
    VIOLATIONS_QUESTION_SECOND_ANSWER = (By.CSS_SELECTOR, 'label[for="violations-0-0"]')

    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, '.email input')

    DISCOUNT_CHECKBOX_ONE = (By.CSS_SELECTOR, 'label[for="currently_employed"]')
    #TODO how do i rotate thees locators ?
    DISCOUNT_CHECKBOX_TWO = (By.CSS_SELECTOR, 'label[for="active_military"]')
    DISCOUNT_CHECKBOX_THREE = (By.CSS_SELECTOR, 'label[for="pay_up_front"]')
    DISCOUNT_CHECKBOX_FOUR = (By.CSS_SELECTOR, 'label[for="auto_pay"]')
    DISCOUNT_CHECKBOX_FIVE = (By.CSS_SELECTOR, 'label[for="paperless"]')

    REFERRAL_INPUT_FIELD = (By.ID, "referral_sourceReferral_sourceInput-0")
        # (By.CSS_SELECTOR, 'label[for="referral_sourceReferral_sourceInput-0"]')
    REFERRAL_FIRST_SELECT = (By.CSS_SELECTOR, '#referral_source-0 div.item:nth-of-type(1)')

    SPOUSE_FIRST_NAME_INPUT_FIELD = (By.CSS_SELECTOR, '.driverPII input#first_name-1')
    SPOUSE_LAST_NAME_INPUT_FIELD = (By.CSS_SELECTOR, '.driverPII input#last_name-1')
    SPOUSE_BIRTH_DATE_INPUT_FIELD = (By.CSS_SELECTOR, '.driverPII input#date_of_birth-1')

    SPOUSE_GENDER_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="gender-0-1"]')
    # TODO {SUBSTRING_OPTION}
    SPOUSE_GENDER_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="gender-1-1"]')

    ANOTHER_DRIVER_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="add_another-1-1"]')
    ANOTHER_DRIVER_QUESTION_RADIO_TWO = (By.CSS_SELECTOR, 'label[for="add_another-0-1"]')

    SHOW_QUOTES_FINAL_CONTINUE_BUTTON = (By.ID, 'summaryShowQuotesBtn')

    def enter_email(self, email):
        self.input(email, *self.EMAIL_INPUT_FIELD)

    def enter_spouse_first_name(self, first):
        self.input(first, *self.SPOUSE_FIRST_NAME_INPUT_FIELD)

    def enter_spouse_last_name(self, last):
        self.input(last, *self.SPOUSE_LAST_NAME_INPUT_FIELD)

    def enter_spouse_dob(self, dob):
        self.input(dob, *self.SPOUSE_BIRTH_DATE_INPUT_FIELD)

    def _get_select_gender_answer_locator(self, option):
        return [self.GENDER_QUESTION_RADIO_ONE[0], self.GENDER_QUESTION_RADIO_ONE[1].replace('{SUBSTRING_OPTION}', option)]

    def select_gender(self, option):
        locator = self._get_select_gender_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_marital_answer_locator(self, option):
        return [self.MARITAL_QUESTION_RADIO_TWO[0], self.MARITAL_QUESTION_RADIO_TWO[1].replace('{SUBSTRING_OPTION}', option)]

    def select_marital(self, option):
        locator = self._get_select_marital_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_credit_answer_locator(self, option):
        return [self.CREDIT_QUESTION_RADIO_TWO[0],  self.CREDIT_QUESTION_RADIO_TWO[1].replace('{SUBSTRING_OPTION}', option)]

    def select_credit(self, option):
        locator = self._get_select_credit_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_education_answer_locator(self, option):
        return [self.EDUCATION_QUESTION_RADIO_FIVE[0], self.EDUCATION_QUESTION_RADIO_FIVE[1].replace('{SUBSTRING_OPTION}', option)]

    def select_education(self, option):
        locator = self._get_select_education_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_duration_answer_locator(self, option):
        return [self.INSURED_QUESTION_RADIO_FOUR[0], self.INSURED_QUESTION_RADIO_FOUR[1].replace('{SUBSTRING_OPTION}', option)]

    def select_duration(self, option):
        locator = self._get_select_duration_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_accidents_answer_locator(self, option):
        return [self.VIOLATIONS_QUESTION_SECOND_ANSWER[0], self.VIOLATIONS_QUESTION_SECOND_ANSWER[1].replace('{SUBSTRING_OPTION}', option)]

    def select_accidents(self, option):
        locator = self._get_select_accidents_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_discounts_answer_locator(self, option):
        return [self.DISCOUNT_CHECKBOX_TWO[0], self.DISCOUNT_CHECKBOX_TWO[1].replace('{SUBSTRING_OPTION}', option)]
    # TODO This step should fall becasue I reused this step twice in the BDD, but assigned only one locator above
    def select_discounts(self, option):
        locator = self._get_select_discounts_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_spouse_gender_answer_locator(self, option):
        return [self.SPOUSE_GENDER_QUESTION_RADIO_TWO[0], self.SPOUSE_GENDER_QUESTION_RADIO_TWO[1].replace('{SUBSTRING_OPTION}', option)]

    def select_spouse_gender(self, option):
        locator = self._get_select_spouse_gender_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_select_additional_driver_answer_locator(self, option):
        return [self.ANOTHER_DRIVER_QUESTION_RADIO_TWO[0], self.ANOTHER_DRIVER_QUESTION_RADIO_TWO[1].replace('{SUBSTRING_OPTION}', option)]


    def select_additional_driver(self, option):
        locator = self._get_select_additional_driver_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    #
    def enter_provider(self, result):
        self.wait_for_element_to_appear(*self.CURRENT_PROVIDER_FIELD)
        self.input(result, *self.CURRENT_PROVIDER_FIELD)
        self.wait_for_element_to_be_clickable_click(*self.CURRENT_PROVIDER_FIRST_SELECT)