from pages.main_page import MainPage
from pages.car_quote_start_page import CarStartPage
from pages.car_quote_vehicles_page import CarVehiclesPage
from pages.car_quote_driver_page import CarDriverOnePage
from pages.car_quote_quote_page import CarQuotePage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.car_quote_start_page = CarStartPage(self.driver)
        self.car_quote_vehicles_page = CarVehiclesPage(self.driver)
        self.car_quote_driver_page = CarDriverOnePage(self.driver)
        self.car_quote_quote_page = CarQuotePage(self.driver)
