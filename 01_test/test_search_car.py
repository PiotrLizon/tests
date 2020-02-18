import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page_object_pattern.pages.search_car import SearchCarPage
from page_object_pattern.pages.search_results import SearchResultsPage
import allure


class TestSearchCar:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    @allure.title('Mobile.de page testing')
    @allure.description('Checking the correctness of names and prices')
    def test_search_chrome(self, setup):
        self.driver.get('https://www.mobile.de/')
        search_car = SearchCarPage(self.driver)
        search_car.set_the_car_brand('Volkswagen')
        search_car.set_the_car_model('Golf')
        search_car.set_the_maximal_price('20000')
        search_car.set_the_maximal_milage('5000')
        search_car.set_year_of_production('2019')
        search_car.search()
        search_car.set_sorting('Neueste Inserate zuerst')

        search_results = SearchResultsPage(self.driver)
        heading_values = search_results.get_headings()
        price_values = search_results.get_prices()

        i = 0
        while i < len(heading_values):
            assert 'Volkswagen Golf' in heading_values[i], 'Invalid heading!'
            i += 1

        j = 0
        while j < len(price_values):
            assert price_values[j] <= 20000, 'Invalid price!'
            j += 1
