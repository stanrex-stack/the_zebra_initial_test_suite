from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CarDriverOnePage(Page):

    GENDER_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="gender-0-0"]')
    GENDER_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="gender-1-0"]')

    MARITAL_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="marital_status-0-0"]')
    MARITAL_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="marital_status-1-0"]')
    MARITAL_QUESTION_RADIO_THREE_LOCATOR = (By.CSS_SELECTOR, 'label[for="marital_status-2-0"]')
    MARITAL_QUESTION_RADIO_FOUR_LOCATOR = (By.CSS_SELECTOR, 'label[for="marital_status-3-0"]')

    CREDIT_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="credit_score-0-0"]')
    CREDIT_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="credit_score-1-0"]')
    CREDIT_QUESTION_RADIO_THREE_LOCATOR = (By.CSS_SELECTOR, 'label[for="credit_score-2-0"]')
    CREDIT_QUESTION_RADIO_FOUR_LOCATOR = (By.CSS_SELECTOR, 'label[for="credit_score-4-0"]')

    EDUCATION_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="education-4-0"]')
    EDUCATION_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="education-3-0"]')
    EDUCATION_QUESTION_RADIO_THREE_LOCATOR = (By.CSS_SELECTOR, 'label[for="education-2-0"]')
    EDUCATION_QUESTION_RADIO_FOUR_LOCATOR = (By.CSS_SELECTOR, 'label[for="education-1-0"]')
    EDUCATION_QUESTION_RADIO_FIVE_LOCATOR = (By.CSS_SELECTOR, 'label[for="education-0-0"]')

    INSURED_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="insured_length-3-0"]')
    INSURED_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="insured_length-2-0"]')
    INSURED_QUESTION_RADIO_THREE_LOCATOR = (By.CSS_SELECTOR, 'label[for="insured_length-1-0"]')
    INSURED_QUESTION_RADIO_FOUR_LOCATOR = (By.CSS_SELECTOR, 'label[for="insured_length-0-0"]')

    CURRENT_PROVIDER_FIELD_LOCATOR = (By.ID, "current_carrierCurrent_carrierInput-0")
        # (By.CSS_SELECTOR, 'label[for="current_carrierCurrent_carrierInput-0"]')
    CURRENT_PROVIDER_FIRST_SELECT_LOCATOR = (By.CSS_SELECTOR, '#current_carrier-0 div.item:nth-of-type(1)')

    VIOLATIONS_QUESTION_FIRST_ANSWER_LOCATOR = (By.CSS_SELECTOR, 'label[for="violations-1-0"]')
    VIOLATIONS_QUESTION_SECOND_ANSWER_LOCATOR = (By.CSS_SELECTOR, 'label[for="violations-0-0"]')

    EMAIL_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, '.email input')

    DISCOUNT_CHECKBOX_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="currently_employed"]')
    DISCOUNT_CHECKBOX_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="active_military"]')
    DISCOUNT_CHECKBOX_THREE_LOCATOR = (By.CSS_SELECTOR, 'label[for="pay_up_front"]')
    DISCOUNT_CHECKBOX_FOUR_LOCATOR = (By.CSS_SELECTOR, 'label[for="auto_pay"]')
    DISCOUNT_CHECKBOX_FIVE_LOCATOR = (By.CSS_SELECTOR, 'label[for="paperless"]')

    REFERRAL_INPUT_FIELD_LOCATOR = (By.ID, "referral_sourceReferral_sourceInput-0")
        # (By.CSS_SELECTOR, 'label[for="referral_sourceReferral_sourceInput-0"]')
    REFERRAL_FIRST_SELECT_LOCATOR = (By.CSS_SELECTOR, '#referral_source-0 div.item:nth-of-type(1)')

    SPOUSE_FIRST_NAME_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, '.driverPII input#first_name-1')
    SPOUSE_LAST_NAME_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, '.driverPII input#last_name-1')
    SPOUSE_BIRTH_DATE_INPUT_FIELD_LOCATOR = (By.CSS_SELECTOR, '.driverPII input#date_of_birth-1')

    SPOUSE_GENDER_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="gender-0-1"]')
    SPOUSE_GENDER_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="gender-1-1"]')

    ANOTHER_DRIVER_QUESTION_RADIO_ONE_LOCATOR = (By.CSS_SELECTOR, 'label[for="add_another-1-1"]')
    ANOTHER_DRIVER_QUESTION_RADIO_TWO_LOCATOR = (By.CSS_SELECTOR, 'label[for="add_another-0-1"]')

    SHOW_QUOTES_FINAL_CONTINUE_BUTTON = (By.ID, 'summaryShowQuotesBtn')


    def element_click(self, element_name):
        if element_name == "Driver Male":
            locator = self.GENDER_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Driver Female":
            locator = self.GENDER_QUESTION_RADIO_TWO_LOCATOR


        elif element_name == "Marital Single":
            locator = self.MARITAL_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Marital Married":
            locator = self.MARITAL_QUESTION_RADIO_TWO_LOCATOR
        elif element_name == "Marital Divorced":
            locator = self.MARITAL_QUESTION_RADIO_THREE_LOCATOR
        elif element_name == "Marital Widowed":
            locator = self.MARITAL_QUESTION_RADIO_FOUR_LOCATOR


        elif element_name == "Credit Excellent (720+)":
            locator = self.CREDIT_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Credit Good (680-719)":
            locator = self.CREDIT_QUESTION_RADIO_TWO_LOCATOR
        elif element_name == "Credit Average (580-679)":
            locator = self.CREDIT_QUESTION_RADIO_THREE_LOCATOR
        elif element_name == "Credit Poor (Below 580)":
            locator = self.CREDIT_QUESTION_RADIO_FOUR_LOCATOR


        elif element_name == "Education Doctoral degree":
            locator = self.EDUCATION_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Education Master's degree":
            locator = self.EDUCATION_QUESTION_RADIO_TWO_LOCATOR
        elif element_name == "Education Bachelor's degree":
            locator = self.EDUCATION_QUESTION_RADIO_THREE_LOCATOR
        elif element_name == "Education High school diploma":
            locator = self.EDUCATION_QUESTION_RADIO_FOUR_LOCATOR
        elif element_name == "Education No diploma":
            locator = self.EDUCATION_QUESTION_RADIO_FIVE_LOCATOR


        elif element_name == "Insured More than 3 years":
            locator = self.INSURED_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Insured 1 to 3 years":
            locator = self.INSURED_QUESTION_RADIO_TWO_LOCATOR
        elif element_name == "Insured 6 to 12 months":
            locator = self.INSURED_QUESTION_RADIO_THREE_LOCATOR
        elif element_name == "Insured Less than 6 months":
            locator = self.INSURED_QUESTION_RADIO_FOUR_LOCATOR


        elif element_name == "Current Provider Input":
            locator = self.CURRENT_PROVIDER_FIELD_LOCATOR
        elif element_name == "Current Provider First Selection":

            locator = self.CURRENT_PROVIDER_FIRST_SELECT_LOCATOR


        elif element_name == "Violations Yes":
            locator = self.VIOLATIONS_QUESTION_FIRST_ANSWER_LOCATOR
        elif element_name == "Violations No":

            locator = self.VIOLATIONS_QUESTION_SECOND_ANSWER_LOCATOR

        elif element_name == "Discount Employed full time":
            locator = self.DISCOUNT_CHECKBOX_ONE_LOCATOR
        elif element_name == "Discount Active military or veteran":
            locator = self.DISCOUNT_CHECKBOX_TWO_LOCATOR
        elif element_name == "Discount Pay in full at the start of policy":
            locator = self.DISCOUNT_CHECKBOX_THREE_LOCATOR
        elif element_name == "Discount Set auto-pay":
            locator = self.DISCOUNT_CHECKBOX_FOUR_LOCATOR
        elif element_name == "Discount Go paperless":
            locator = self.DISCOUNT_CHECKBOX_FIVE_LOCATOR


        elif element_name == "Referral Input":
            locator = self.REFERRAL_INPUT_FIELD_LOCATOR
        elif element_name == "Referral First Selection":
            locator = self.REFERRAL_FIRST_SELECT_LOCATOR

        elif element_name == "Spouse Male":
            locator = self.SPOUSE_GENDER_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Spouse Female":
            locator = self.SPOUSE_GENDER_QUESTION_RADIO_TWO_LOCATOR


        elif element_name == "Add Driver Yes":
            locator = self.ANOTHER_DRIVER_QUESTION_RADIO_ONE_LOCATOR
        elif element_name == "Add Driver No":
            locator = self.ANOTHER_DRIVER_QUESTION_RADIO_TWO_LOCATOR


        elif element_name == "Show My Quotes":
            locator = self.SHOW_QUOTES_FINAL_CONTINUE_BUTTON

        else:
            raise Exception("No such field name found")
        sleep(1)
        self.wait_for_element_to_be_clickable_click(*locator)
        sleep(1)

    def input_information(self, element_string, input_text):

        if element_string == 'Spouse First Name':
            locator_1 = self.SPOUSE_FIRST_NAME_INPUT_FIELD_LOCATOR
        elif element_string == 'Spouse Last Name':
            locator_1 = self.SPOUSE_LAST_NAME_INPUT_FIELD_LOCATOR
        elif element_string == "Spouse Birthdate":
            locator_1 = self.SPOUSE_BIRTH_DATE_INPUT_FIELD_LOCATOR

        elif element_string == "Email":
            locator_1 = self.EMAIL_INPUT_FIELD_LOCATOR

        else:
            raise Exception("No such field name found")
        self.wait_for_element_to_be_clickable_click(*locator_1)
        self.input(input_text, *locator_1)