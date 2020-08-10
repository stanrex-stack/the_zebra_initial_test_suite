from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CarVehiclesPage(Page):

    VEHICLE_YEAR_INPUT = (By.CSS_SELECTOR, '.vehicle-select #yearYear-0Input-0')
    VEHICLE_FIRST_RESULT = (By.CSS_SELECTOR, 'div.dropdown-menu.show:nth-of-type(1) div.item:nth-of-type(1)')

    VEHICLE_NAME_INPUT = (By.ID, 'makeMake-0Input-0')
    VEHICLE_MODEL_INPUT = (By.ID, 'modelModel-0Input-0')

    VEHICLE_SUBMODEL_INPUT = (By.ID, 'submodelSubmodel-0Input-0')

    SAVE_AND_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.btn-continue')

    FIRST_QUESTION_FIRST_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="ownership-0-0"]')
    FIRST_QUESTION_SECOND_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="ownership-2-0"]')
    FIRST_QUESTION_THIRD_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="ownership-1-0"]')

    SECOND_QUESTION_FIRST_RADIO_BUTTON= (By.CSS_SELECTOR, 'label[for="primary_use-0-0"]')
    SECOND_QUESTION_SECOND_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="primary_use-1-0"]')
    SECOND_QUESTION_THIRD_RADIO_BUTTON =(By.CSS_SELECTOR, 'label[for="primary_use-4-0"]')
    SECOND_QUESTION_FOURTH_RADIO_BUTTON = (By.CSS_SELECTOR, 'label[for="primary_use-2-0"]')

    MILAGE_INPUT_LOCATOR = (By.ID, 'miles-input-0')


    def enter_car_year(self, year):
        self.wait_for_element_to_appear(*self.VEHICLE_YEAR_INPUT)
        self.input(year, *self.VEHICLE_YEAR_INPUT)
        self.wait_for_element_to_be_clickable_click(*self.VEHICLE_FIRST_RESULT)


    def enter_car_make(self, car):
        self.wait_for_element_to_appear(*self.VEHICLE_NAME_INPUT)
        self.input(car, *self.VEHICLE_NAME_INPUT)
        self.wait_for_element_to_be_clickable_click(*self.VEHICLE_FIRST_RESULT)

    def enter_car_model(self, model):
        self.wait_for_element_to_appear(*self.VEHICLE_MODEL_INPUT)
        self.input(model, *self.VEHICLE_MODEL_INPUT)
        self.wait_for_element_to_be_clickable_click(*self.VEHICLE_FIRST_RESULT)

    def enter_car_trim(self, trim):
        self.wait_for_element_to_appear(*self.VEHICLE_MODEL_INPUT)
        self.input(trim, *self.VEHICLE_MODEL_INPUT)
        self.wait_for_element_to_be_clickable_click(*self.VEHICLE_FIRST_RESULT)

    def click_continue(self):
        e = self.wait_for_element_to_appear(*self.SAVE_AND_CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        self.wait_for_element_to_be_clickable_click(*self.SAVE_AND_CONTINUE_BUTTON)

    def _get_own_car_answer_locator(self, option):
        return [self.FIRST_QUESTION_FIRST_RADIO_BUTTON[0], self.FIRST_QUESTION_FIRST_RADIO_BUTTON[1].replace('{SUBSTRING_OPTION}', option)]
    # TODO PLEASE SEE THIS AND THE LOCATORS
    def select_if_own_car(self, option):
        locator = self._get_own_car_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def _get_car_usage_answer_locator(self, option):
        return [self.SECOND_QUESTION_FOURTH_RADIO_BUTTON[0], self.SECOND_QUESTION_FOURTH_RADIO_BUTTON[1].replace('{SUBSTRING_OPTION}', option)]
    # TODO PLEASE SEE THIS AND THE LOCATORS
    def select_car_usage(self, option):
        locator = self._get_car_usage_answer_locator(option)
        self.wait_for_element_to_be_clickable_click(*locator)

    def enter_car_milage(self, milage):
        self.wait_for_element_to_appear(*self.MILAGE_INPUT_LOCATOR)
        self.input(milage, *self.MILAGE_INPUT_LOCATOR)
        self.wait_for_element_to_be_clickable_click(*self.MILAGE_INPUT_LOCATOR)

