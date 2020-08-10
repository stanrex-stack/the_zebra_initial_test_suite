from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from features.logger import logger


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.thezebra.com/'
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.actions = ActionChains(self.driver)
        self.alerts = Alert(self.driver)

    def open_page(self, url = ''):
        logger.info(f'Opened page {url}')
        self.driver.get(self.base_url + url)

    def click(self, *locator):
        logger.info(f'found element {locator}')
        self.driver.find_element(*locator).click()

    def input(self, text: str, *locator):
        input_field = self.driver.find_element(*locator)
        # input_field.clear()
        input_field.send_keys(text)

    def verify_element_text(self, expected_text: str, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f'Expexcted {expected_text}, but got {actual_text}'

    def get_attribute_value(self, attribute_name: str, *locator):
        element = self.driver.find_element(*locator)
        attribute_value = element.get_attribute(attribute_name)
        return attribute_value

    def hover_over_element(self, *locator):
        locator_var = self.driver.find_element(*locator)
        self.actions.move_to_element(locator_var).perform()

    def select_by_name(self, visible_text: str, *locator):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(visible_text)

    def click_on_list_element(self, expected_index: int, *locator):
        list_locator = self.driver.find_elements(*locator)
        list_locator[expected_index].click()

    def verify_element_count(self, expected_number, *locator ):
        actual_number = int(len(self.driver.find_elements(*locator)))
        assert actual_number == int(expected_number), f'Expected {expected_number}, but got {actual_number} elements'

    def wait_for_element_to_be_clickable_click(self, *locator):
        element_to_click = self.driver.wait.until(EC.element_to_be_clickable(locator))
        element_to_click.click()

    def wait_for_element_to_be_clickable(self, *locator):
        self.driver.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_element_to_disappear(self, *locator):
        self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_to_appear(self, *locator):
        self.driver.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_element_to_be_located(self, *locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_for_all_elements_located(self, *locator):
        self.driver.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until_alert_is_present(self):
        return self.driver.wait.until(EC.alert_is_present())
