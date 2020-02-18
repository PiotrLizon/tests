import logging
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select
import allure


class SearchCarPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.brand_select_xpath = '//*[@id="qsmakeBuy"]'
        self.model_select_xpath = '//*[@id="qsmodelBuy"]'
        self.max_price_xpath = '//*[@id="qsprc"]'
        self.max_milage_xpath = '//*[@id="qsmil"]'
        self.year_xpath = '//*[@id="qsfrg"]'
        self.search_xpath = '//*[@id="qssub"]'
        self.sorting_xpath = '//*[@id="so-sb"]'

    @allure.step('Setting car brand to {1}')
    def set_the_car_brand(self, brand):
        self.logger.info('Setting the car brand {}'.format(brand))
        brand_select = Select(self.driver.find_element_by_xpath(self.brand_select_xpath))
        brand_select.select_by_visible_text(brand)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_the_car_brand', attachment_type=AttachmentType.PNG)

    @allure.step('Setting the car model to {1}')
    def set_the_car_model(self, model):
        self.logger.info('Setting the car model {}'.format(model))
        model_select = Select(self.driver.find_element_by_xpath(self.model_select_xpath))
        model_select.select_by_visible_text(model)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_the_car_model', attachment_type=AttachmentType.PNG)

    @allure.step('Setting the maximal price to {1}')
    def set_the_maximal_price(self, price):
        self.logger.info('Setting the maximal price {}'.format(price))
        self.driver.find_element_by_xpath(self.max_price_xpath).send_keys(price)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_the_maximal_price', attachment_type=AttachmentType.PNG)

    @allure.step('Setting the maximal milage to {1}')
    def set_the_maximal_milage(self, milage):
        self.logger.info('Setting the maximal milage {}'.format(milage))
        self.driver.find_element_by_xpath(self.max_milage_xpath).send_keys(milage)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_the_maximal_milage', attachment_type=AttachmentType.PNG)

    @allure.step('Setting year of production to {1}')
    def set_year_of_production(self, year):
        self.logger.info('Setting year {}'.format(year))
        self.driver.find_element_by_xpath(self.year_xpath).send_keys(year)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_year', attachment_type=AttachmentType.PNG)

    def search(self):
        self.logger.info('Searching')
        self.driver.find_element_by_xpath(self.search_xpath).click()

    @allure.step('Setting sorting to {1}')
    def set_sorting(self, sort):
        self.logger.info('Setting sorting {}'.format(sort))
        sorting_select = Select(self.driver.find_element_by_xpath(self.sorting_xpath))
        sorting_select.select_by_visible_text(sort)
        allure.attach(self.driver.get_screenshot_as_png(), name='set_sorting', attachment_type=AttachmentType.PNG)
