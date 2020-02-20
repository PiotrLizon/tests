import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random


class RegistrationPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.sign_in_text = 'Sign in'
        self.email_name = 'email_create'
        self.sex_name = 'id_gender'
        self.first_name = 'customer_firstname'
        self.last_name = 'customer_lastname'
        self.password_name = 'passwd'
        self.days_name = 'days'
        self.months_name = 'months'
        self.years_name = 'years'
        self.company_name = 'company'
        self.newsletter_one_name = 'newsletter'
        self.newsletter_two_name = 'optin'
        self.address_name = 'address1'
        self.city_name = 'city'
        self.state_name = 'id_state'
        self.postcode_name = 'postcode'
        self.phone_name = 'phone'
        self.mobile_phone_name = 'phone_mobile'
        self.submit_name = 'submitAccount'
        self.positive_result_class = 'info-account'
        self.negative_result_xpath = '//*[@id="center_column"]/div/p'

    @allure.step('Turning on the form with {1}')
    def turning_on_the_form(self, email):
        self.logger.info('Turning on the form with {}'.format(email))
        self.driver.find_element_by_partial_link_text(self.sign_in_text).click()
        random_number = str(random.randrange(10 ** 5))
        user_email = random_number + email
        self.driver.find_element_by_name(self.email_name).send_keys(user_email)
        self.driver.find_element_by_name(self.email_name).send_keys(Keys.ENTER)
        allure.attach(self.driver.get_screenshot_as_png(), name="turn_form_on", attachment_type=AttachmentType.PNG)

    @allure.step('Setting account information: {1}, {2}, {3}')
    def set_account_information(self, name, last_name, password):
        self.logger.info('Setting account information: {}, {}, {}'.format(name, last_name, password))
        self.driver.find_element_by_name(self.sex_name).click()
        self.driver.find_element_by_name(self.first_name).send_keys(name)
        self.driver.find_element_by_name(self.last_name).send_keys(last_name)
        self.driver.find_element_by_name(self.password_name).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_account", attachment_type=AttachmentType.PNG)

    @allure.step('Setting date og birth: {1}, {2}, {3}')
    def set_the_date_of_birth(self, day, month, year):
        self.logger.info('Setting date og birth: {}, {}, {}'.format(day, month, year))
        day_select = Select(self.driver.find_element_by_name(self.days_name))
        day_select.select_by_value(day)
        month_select = Select(self.driver.find_element_by_name(self.months_name))
        month_select.select_by_value(month)
        year_select = Select(self.driver.find_element_by_name(self.years_name))
        year_select.select_by_value(year)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_the_date", attachment_type=AttachmentType.PNG)

    @allure.step('Setting notifications')
    def set_notifications(self):
        self.logger.info('Setting notifications')
        self.driver.find_element_by_name(self.newsletter_one_name).click()
        self.driver.find_element_by_name(self.newsletter_two_name).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_notifications", attachment_type=AttachmentType.PNG)

    @allure.step('Setting account address: {1}, {2}, {3}, {4}, {5}')
    def set_account_address(self, company, address, city, state, postcode):
        self.logger.info('Setting account address: {}, {}, {}, {}, {}'.format(company, address, city, state, postcode))
        self.driver.find_element_by_name(self.company_name).send_keys(company)
        self.driver.find_element_by_name(self.address_name).send_keys(address)
        self.driver.find_element_by_name(self.city_name).send_keys(city)
        state_select = Select(self.driver.find_element_by_name(self.state_name))
        state_select.select_by_visible_text(state)
        self.driver.find_element_by_name(self.postcode_name).send_keys(postcode)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_address", attachment_type=AttachmentType.PNG)

    @allure.step('Setting the phone numbers: {1}, {2}')
    def set_the_phone_numbers(self, number, mobile_number):
        self.logger.info('Setting the phone numbers: {}, {}'.format(number, mobile_number))
        self.driver.find_element_by_name(self.phone_name).send_keys(number)
        self.driver.find_element_by_name(self.mobile_phone_name).send_keys(mobile_number)
        self.driver.find_element_by_name(self.submit_name).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_the_date", attachment_type=AttachmentType.PNG)

    @allure.step('Checking positive result')
    def checking_positive_result(self):
        self.logger.info('Checking positive result')
        result = self.driver.find_element_by_class_name(self.positive_result_class).text
        self.logger.info(result)
        allure.attach(self.driver.get_screenshot_as_png(), name="checking", attachment_type=AttachmentType.PNG)
        return result

    @allure.step('Checking negative result')
    def checking_negative_result(self):
        self.logger.info('Checking negative result')
        result = self.driver.find_element_by_xpath(self.negative_result_xpath).text
        self.logger.info(result)
        return result
