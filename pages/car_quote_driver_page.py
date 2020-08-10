from pages.base_page import Page
from selenium.webdriver.common.by import By


class CarDriverOnePage(Page):
    QUESTIONS = (By.CSS_SELECTOR, 'h3.question-text')
    GENDER_MALE = (By.CSS_SELECTOR, 'label[for="gender-0-0"]')
    GENDER_FEMALE = (By.CSS_SELECTOR, 'label[for="gender-1-0"]')
    GENDER_SELECTED = (By.CSS_SELECTOR, "div#gender-0 span.complete")
    MARITAL_STATUS_ANSWER = (By.CSS_SELECTOR, 'label[data-cy*="{MARITAL_STATUS}"][for*="marital_status"]')
    MARITAL_STATUS_SELECTED = (By.CSS_SELECTOR, 'div#marital_status-0 span.complete')
    CREDIT_SCORE = (By.CSS_SELECTOR, 'label[data-cy*="{SCORE}"][for*="score"]')
    CREDIT_SCORE_SELECTED = (By.CSS_SELECTOR, 'div#credit_score-0 span.complete')
    EDUCATION = (By.CSS_SELECTOR, 'label[data-cy*="{EDUCATION_LEVEL}"][for*="education"]')
    EDUCATION_SELECTED = (By.CSS_SELECTOR, 'div#education-0 span.complete')
    INSURED_QUESTION_RADIO_ONE = (By.CSS_SELECTOR, 'label[for="insured_length-3-0"]')
    INSURED_ANSWERED = (By.CSS_SELECTOR, 'div#insured_length-0 span.complete')

    CURRENT_PROVIDER_FIELD = (By.ID, "current_carrierCurrent_carrierInput-0")
    CURRENT_PROVIDER_FIRST_SELECT = (By.CSS_SELECTOR, '#current_carrier-0 div.item:nth-of-type(1)')
    CURRENT_PROVIDER_SELECTED = (By.CSS_SELECTOR, "div#current_carrier-0 span.complete")
    ANY_ACCIDENTS_ANSWER = (By.CSS_SELECTOR, 'label[for="violations-{SUBSTRING_OPTION}-0"]')

    EMAIL_INPUT_FIELD = (By.CSS_SELECTOR, '.email input')
    SHOW_QUOTES_BUTTON = (By.ID, 'summaryShowQuotesBtn')

    def _get_select_marital_answer_locator(self, option):
        return [self.MARITAL_STATUS_ANSWER[0], self.MARITAL_STATUS_ANSWER[1].replace('{MARITAL_STATUS}', option)]

    def _get_select_credit_answer_locator(self, option):
        return [self.CREDIT_SCORE[0], self.CREDIT_SCORE[1].replace('{SCORE}', option)]

    def _get_select_education_answer_locator(self, option):
        return [self.EDUCATION[0], self.EDUCATION[1].replace('{EDUCATION_LEVEL}', option)]

    def _get_select_accidents_answer_locator(self, option):
        return [self.ANY_ACCIDENTS_ANSWER[0], self.ANY_ACCIDENTS_ANSWER[1].replace('{SUBSTRING_OPTION}', option)]

    def select_gender(self, option):
        self.wait_for_element_to_appear(*self.GENDER_MALE)
        self.wait_for_all_elements_located(*self.QUESTIONS)
        if option == 'male':
            self.wait_for_element_to_be_clickable_click(*self.GENDER_MALE)
        elif option == 'female':
            self.wait_for_element_to_be_clickable_click(*self.GENDER_FEMALE)
        self.wait_for_element_to_be_located(*self.GENDER_SELECTED)

    def select_marital_status(self, option):
        locator = self._get_select_marital_answer_locator(option.capitalize())
        self.wait_for_element_to_be_clickable_click(*locator)
        self.wait_for_element_to_appear(*self.MARITAL_STATUS_SELECTED)

    def select_credit(self, option):
        self.wait_for_all_elements_located(*self.QUESTIONS)
        locator = self._get_select_credit_answer_locator(option.capitalize())
        self.wait_for_element_to_be_clickable_click(*locator)
        self.wait_for_element_to_appear(*self.CREDIT_SCORE_SELECTED)

    def select_education(self, option):
        self.wait_for_all_elements_located(*self.QUESTIONS)
        locator = self._get_select_education_answer_locator(option.capitalize())
        self.wait_for_element_to_be_clickable_click(*locator)
        self.wait_for_element_to_appear(*self.EDUCATION_SELECTED)

    def select_duration(self, option):
        self.wait_for_all_elements_located(*self.QUESTIONS)
        # Just hardcoding to option 1
        self.wait_for_element_to_be_clickable_click(*self.INSURED_QUESTION_RADIO_ONE)
        self.wait_for_element_to_appear(*self.INSURED_ANSWERED)

    def select_accidents(self, option):
        self.wait_for_all_elements_located(*self.QUESTIONS)
        if option == 'no':
            option = '0'
        elif option == 'yes':
            option = '1'
        locator = self._get_select_accidents_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def enter_provider(self, provider):
        e = self.wait_for_element_to_appear(*self.CURRENT_PROVIDER_FIELD)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        self.wait_for_element_to_be_clickable_click(*self.CURRENT_PROVIDER_FIELD)

        self.input(provider, *self.CURRENT_PROVIDER_FIELD)
        self.wait_for_certain_amount_of_elements(1, *self.CURRENT_PROVIDER_FIRST_SELECT)
        self.wait_for_element_to_be_clickable_click(*self.CURRENT_PROVIDER_FIRST_SELECT)
        self.wait_for_element_to_appear(*self.CURRENT_PROVIDER_SELECTED)

    def enter_email(self, email):
        self.wait_for_element_to_appear(*self.EMAIL_INPUT_FIELD)
        self.input(email, *self.EMAIL_INPUT_FIELD)

    def click_show_quotes(self):
        self.wait_for_element_to_be_clickable_click(*self.SHOW_QUOTES_BUTTON)