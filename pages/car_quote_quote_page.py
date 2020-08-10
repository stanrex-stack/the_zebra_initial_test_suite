from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
#TODO this places is a mess I am sorry
class CarQuotePage(Page):

    TITLES_ARRAY = (By.CSS_SELECTOR, 'h4.carrier-name')
    QUOTES_ARRAY = (By.CSS_SELECTOR, '.btn-primary')
    CARRIER_CARD = (By.CSS_SELECTOR, 'div.carrier-info')
    WRAPPER = (By.CSS_SELECTOR, '.carrier-cards-wrapper')

    def gather_all_quotes_1(self):
        j = self.driver.find_elements(*self.TITLES_ARRAY)
        for i in j:
            print(i.text)

        k = self.driver.find_elements(*self.QUOTES_ARRAY)
        for i in k:
            print(i.text)


    def gather_all_quotes(self):
        dict_1 = {}
        wrapper = self.driver.find_element(*self.WRAPPER)

        items = wrapper.find_elements(*self.CARRIER_CARD)

        for item in items:

            titels = item.find_element(*self.TITLES_ARRAY)
            not_titles = item.find_element(*self.QUOTES_ARRAYR)
            dict_1[titels.text] = not_titles.text

        print(dict_1)
