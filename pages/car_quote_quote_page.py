from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class CarQuotePage(Page):

    TITLES_ARRAY_LOCATOR = (By.CSS_SELECTOR, 'h4.carrier-name')
    QUOTES_ARRAY_LOCATOR = (By.CSS_SELECTOR, '.btn-primary')
    CARRIER_CARD_LOCATOR = (By.CSS_SELECTOR, 'div.carrier-info')
    WRAPPER_LOCATOR = (By.CSS_SELECTOR, '.carrier-cards-wrapper')

    def gather_all_quotes_1(self):
        j = self.driver.find_elements(*self.TITLES_ARRAY_LOCATOR)
        for i in j:
            print(i.text)

        k = self.driver.find_elements(*self.QUOTES_ARRAY_LOCATOR)
        for i in k:
            print(i.text)

    # def find_index(self):
    #     index = len(self.driver.find_elements(*self.CARRIER_CARD_LOCATOR))
    #     print(index)
    #     return index

    def gather_all_quotes(self):
        dict_1 = {}
        wrapper = self.driver.find_element(*self.WRAPPER_LOCATOR)
        # print(wrapper)
        # length = len(wrapper.find_elements(*self.CARRIER_CARD_LOCATOR))
        # print(length)
        items = wrapper.find_elements(*self.CARRIER_CARD_LOCATOR)

        for item in items:
            # quote = items[item]
            titels = item.find_element(*self.TITLES_ARRAY_LOCATOR)
            not_titles = item.find_element(*self.QUOTES_ARRAY_LOCATOR)
            dict_1[titels.text] = not_titles.text
        # dict_1 = {}
        # for item in range(0, index):
        #     j = self.driver.find_element(*self.CARRIER_CARD_LOCATOR)[item]
        #     print(j)
        #     for i in j:
        #         print(i)
        #         title = i.find_element(*self.TITLES_ARRAY_LOCATOR)
        #         quote = i.find_element(*self.CARRIER_CARD_LOCATOR)
        #         dict_1[title] = quote
        print(dict_1)
