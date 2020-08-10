from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CarQuotePage(Page):
    TITLES_ARRAY = (By.CSS_SELECTOR, 'h4.carrier-name')

    def verify_quotes_shown(self):
        wait = WebDriverWait(self.driver, 50)
        wait.until(EC.url_to_be('https://www.thezebra.com/z/rate-select/'))
        wait.until(EC.presence_of_all_elements_located(self.TITLES_ARRAY))

        # Print out quotes providers
        print('Quotes found:')
        print([t.text for t in self.driver.find_elements(*self.TITLES_ARRAY)])
