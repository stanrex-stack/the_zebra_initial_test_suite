from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class CarVehiclesPage(Page):
    VEHICLE_YEAR_INPUT = (By.CSS_SELECTOR, '.vehicle-select #yearYear-0Input-0')
    DROP_DOWN_ITEM = (By.CSS_SELECTOR, "div.dropdown-menu.show div[role='menuitem']")
    VEHICLE_NAME_INPUT = (By.ID, 'makeMake-0Input-0')
    VEHICLE_MODEL_INPUT = (By.ID, 'modelModel-0Input-0')
    VEHICLE_SUBMODEL_INPUT = (By.ID, 'submodelSubmodel-0Input-0')
    SAVE_AND_CONTINUE_BUTTON = (By.CSS_SELECTOR, '.btn-continue')
    VEHICLE_DETAIL_ANSWER = (By.CSS_SELECTOR, 'label[data-cy*="{SUBSTRING_OPTION}"]')
    VEHICLE_DETAIL_SELECTED = (By.CSS_SELECTOR, "div#primary_use-0 span.complete")
    MILEAGE_INPUT_FIELD = (By.ID, 'miles-input-0')

    def _get_car_answer_locator(self, option):
        return [self.VEHICLE_DETAIL_ANSWER[0], self.VEHICLE_DETAIL_ANSWER[1].replace('{SUBSTRING_OPTION}', option)]

    def enter_car_year(self, year):
        self.wait_for_element_to_be_clickable(*self.VEHICLE_YEAR_INPUT)
        self.input(year, *self.VEHICLE_YEAR_INPUT)
        self.wait_for_certain_amount_of_elements(1, *self.DROP_DOWN_ITEM)
        self.input(Keys.ENTER, *self.VEHICLE_YEAR_INPUT)

    def enter_car_make(self, car):
        self.wait_for_element_to_be_clickable(*self.VEHICLE_NAME_INPUT)
        self.input(car, *self.VEHICLE_NAME_INPUT)
        self.wait_for_certain_amount_of_elements(1, *self.DROP_DOWN_ITEM)
        self.input(Keys.ENTER, *self.VEHICLE_NAME_INPUT)

    def enter_car_model(self, model):
        self.wait_for_element_to_be_clickable(*self.VEHICLE_MODEL_INPUT)
        self.input(model, *self.VEHICLE_MODEL_INPUT)
        sleep(1)
        self.wait_for_certain_amount_of_elements(1, *self.DROP_DOWN_ITEM)
        self.input(Keys.ENTER, *self.VEHICLE_MODEL_INPUT)

    def enter_car_trim(self, trim):
        e = self.wait_for_element_to_appear(*self.VEHICLE_SUBMODEL_INPUT)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        self.wait_for_element_to_be_clickable(*self.VEHICLE_SUBMODEL_INPUT)
        self.input(trim, *self.VEHICLE_SUBMODEL_INPUT)
        sleep(1)
        self.wait_for_certain_amount_of_elements(1, *self.DROP_DOWN_ITEM)
        self.input(Keys.ENTER, *self.VEHICLE_SUBMODEL_INPUT)

    def click_continue(self):
        e = self.wait_for_element_to_appear(*self.SAVE_AND_CONTINUE_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", e)
        self.wait_for_element_to_be_clickable_click(*self.SAVE_AND_CONTINUE_BUTTON)

    def select_if_own_car(self, option):
        option, valid_answers = option.lower(), ['paid in full', 'making payments', 'lease']
        if option == 'paid in full':
            option = 'Own-PaidInFull'
        elif option == 'making payments':
            option = 'Own-MakingPayments'
        elif option == 'lease':
            option = 'Lease'
        else:
            raise ValueError(f"{option} not a valid answer, {valid_answers}")
        locator = self._get_car_answer_locator(option)
        sleep(1)
        self.wait_for_element_to_be_clickable_click(*locator)

    def select_car_usage(self, option):
        option, valid_answers = option.lower(), ['personal/commuting', 'pleasure', 'farm', 'business/rideshare']
        if option == 'personal/commuting':
            option = 'Personal/Commuting'
        elif option == 'pleasure':
            option = 'Pleasure'
        elif option == 'farm':
            option = 'Farm'
        elif option == 'business/rideshare':
            option = 'Business/Rideshare'
        else:
            raise ValueError(f"{option} not a valid answer, {valid_answers}")
        locator = self._get_car_answer_locator(option)
        sleep(1)
        self.wait_for_element_to_be_clickable_click(*locator)
        self.wait_for_element_to_appear(*self.VEHICLE_DETAIL_SELECTED)

    def enter_car_mileage(self, mileage):
        self.wait_for_element_to_appear(*self.MILEAGE_INPUT_FIELD)
        self.input(mileage, *self.MILEAGE_INPUT_FIELD)
        self.wait_for_element_to_be_clickable_click(*self.MILEAGE_INPUT_FIELD)
