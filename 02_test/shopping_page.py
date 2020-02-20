import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.select import Select


class ShoppingPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.women_btn_class = 'sf-with-ul'
        self.dresses_btn_xpath = '//*[@id="subcategories"]/ul/li[2]/div[1]/a/img'
        self.dress_btn_xpath = '//*[@id="center_column"]/ul/li[1]/div/div[1]/div/a[1]/img'
        self.add_to_cart_xpath = '//*[@id="add_to_cart"]/button'
        self.continue_btn_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span'
        self.select_size_xpath = '//*[@id="group_1"]'
        self.proceed_to_checkout_xpath = '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a/span'
        self.dress_size_s_xpath = '//*[@id="product_3_13_0_0"]/td[2]/small[2]/a'
        self.dress_size_l_xpath = '//*[@id="product_3_15_0_0"]/td[2]/small[2]/a'
        self.dress_name_xpath = '//*[@id="product_3_13_0_0"]/td[2]/p/a'

    @allure.step('Turning on the store')
    def turning_on_the_store(self):
        self.logger.info('Turning on the store')
        self.driver.find_element_by_class_name(self.women_btn_class).click()
        self.driver.find_element_by_xpath(self.dresses_btn_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="turn_store_on", attachment_type=AttachmentType.PNG)

    @allure.step('Adding the dress to cart')
    def adding_the_dress_to_cart(self):
        self.logger.info('Adding the dress to cart')
        self.driver.find_element_by_xpath(self.dress_btn_xpath).click()
        self.driver.find_element_by_xpath(self.add_to_cart_xpath).click()
        self.driver.find_element_by_xpath(self.continue_btn_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="dress_to_cart", attachment_type=AttachmentType.PNG)

    @allure.step('Adding a different size {1}')
    def adding_a_different_size(self, index):
        self.logger.info('Adding a different size {}'.format(index))
        dress_size = Select(self.driver.find_element_by_xpath(self.select_size_xpath))
        dress_size.select_by_index(index)
        self.driver.find_element_by_xpath(self.add_to_cart_xpath).click()
        self.driver.find_element_by_xpath(self.proceed_to_checkout_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="different_size", attachment_type=AttachmentType.PNG)

    @allure.step('Checking the order')
    def checking_the_order(self):
        self.logger.info('Checking the order')
        size_one = self.driver.find_element_by_xpath(self.dress_size_s_xpath).text
        size_two = self.driver.find_element_by_xpath(self.dress_size_l_xpath).text
        dress_name = self.driver.find_element_by_xpath(self.dress_name_xpath).text
        allure.attach(self.driver.get_screenshot_as_png(), name="checking", attachment_type=AttachmentType.PNG)
        return size_one, size_two, dress_name
