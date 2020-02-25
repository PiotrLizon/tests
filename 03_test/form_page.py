import logging


class FormPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.submit_btn_xpath = '//*[@id="content"]/div/div[3]/div[2]/div/form/div[5]/button[1]'
        self.username_msg_xpath = '//*[@id="content"]/div/div[3]/div[2]/div/form/div[1]/div/span'
        self.email_xpath = '//*[@id="content"]/div/div[3]/div[2]/div/form/div[2]/div/span'
        self.age_msg_xpath = '//*[@id="content"]/div/div[3]/div[2]/div/form/div[3]/div/span'
        self.phone_msg_xpath = '//*[@id="content"]/div/div[3]/div[2]/div/form/div[4]/div/span'
        self.username_name = 'username'
        self.email_name = 'email'
        self.age_name = 'age'
        self.phone_name = 'phone'

    def submit(self):
        self.logger.info('approval')
        self.driver.find_element_by_xpath(self.submit_btn_xpath).click()

    def get_msgs(self):
        self.logger.info('getting messages:')
        username_var = self.driver.find_element_by_xpath(self.username_msg_xpath).text
        age_var = self.driver.find_element_by_xpath(self.age_msg_xpath).text
        phone_number_var = self.driver.find_element_by_xpath(self.phone_msg_xpath).text
        values = username_var, age_var, phone_number_var
        self.logger.info(values)
        return username_var, age_var, phone_number_var

    def get_msg(self):
        self.logger.info('getting message:')
        email_var = self.driver.find_element_by_xpath(self.email_xpath).text
        self.logger.info(email_var)
        return email_var

    def filling_the_form(self, username, email, age, phone_number):
        self.logger.info('Filling the form {} {} {} {}'.format(username, email, age, phone_number))
        self.driver.find_element_by_name(self.username_name).send_keys(username)
        self.driver.find_element_by_name(self.email_name).send_keys(email)
        self.driver.find_element_by_name(self.age_name).send_keys(age)
        self.driver.find_element_by_name(self.phone_name).send_keys(phone_number)
