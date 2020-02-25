import logging
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


class PhptravelsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.login_css = 'div.dropdown-login a.btn'
        self.drop_down_login_css = 'div a.dropdown-item.active'
        self.username_name = 'username'
        self.password_name = 'password'
        self.login_btn_xpath = '//*[@id="loginfrm"]/button'
        self.welcome_msg_xpath = 'div.col-md-8 h3.text-align-left'
        self.contact_page_xpath = '//*[@id="mobileMenuMain"]/nav/ul[2]/li[6]/a'
        self.contact_btn_name = 'Contact'
        self.contact_page_title_css = 'div.container h2.float-none'
        self.form_name_id = 'form_name'
        self.form_email_id = 'form_email'
        self.form_subject_id = 'form_subject'
        self.form_message_id = 'form_message'
        self.form_submit_name = 'submit_contact'
        self.alert_name = 'alert'

    @allure.step('Logging using: {1}, {2}')
    def log_in(self, username, password):
        self.logger.info('Logging using: {} {}'.format(username, password))
        self.driver.find_element_by_css_selector(self.login_css).click()
        self.driver.find_element_by_css_selector(self.drop_down_login_css).click()
        self.driver.find_element_by_name(self.username_name).send_keys(username)
        self.driver.find_element_by_name(self.password_name).send_keys(password)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name='log_in')
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()

    @allure.step('Getting welcome massage.')
    def get_welcome_message(self):
        self.logger.info('Getting welcome massage:')
        welcome = self.driver.find_element_by_css_selector(self.welcome_msg_xpath).text
        self.logger.info(welcome)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name='welcome_msg')
        return welcome

    @allure.step('Opening the form.')
    def open_the_form(self):
        self.logger.info('Opening the form.')
        contact_page = self.driver.find_element_by_xpath(self.contact_page_xpath)
        webdriver.ActionChains(self.driver).move_to_element(contact_page).perform()
        self.driver.find_element_by_link_text(self.contact_btn_name).click()
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name='open_form')

    @allure.step('Getting contact page title.')
    def get_contact_page_title(self):
        self.logger.info('Getting contact page title:')
        contact_h2 = self.driver.find_element_by_css_selector(self.contact_page_title_css).text
        self.logger.info(contact_h2)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name='get_title')
        return contact_h2

    @allure.step('Filling out the form with: {1}, {2}, {3}, {4}')
    def fill_out_the_form(self, name, email, subject, message):
        self.logger.info('Filling out the form with: {}, {}, {}, {}'.format(name, email, subject, message))
        self.driver.find_element_by_id(self.form_name_id ).send_keys(name)
        self.driver.find_element_by_id(self.form_email_id).send_keys(email)
        self.driver.find_element_by_id(self.form_subject_id).send_keys(subject)
        self.driver.find_element_by_id(self.form_message_id).send_keys(message)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name='fill_out_form')
        self.driver.find_element_by_name(self.form_submit_name).click()

    @allure.step('Getting the alert.')
    def get_the_alert(self):
        self.logger.info('Getting the alert:')
        alert = self.driver.find_element_by_class_name(self.alert_name).text
        self.logger.info(alert)
        allure.attach(self.driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name='get_alert')
        return alert
