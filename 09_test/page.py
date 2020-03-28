import logging
from selenium.webdriver.support.select import Select
import formulas


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.banner_css = 'div.banner_banner--3pjXd'
        self.banner_accept_css = 'a.banner_continue--2NyXA'
        self.btn_calculate_css = 'button.btn-calculate'
        self.distance_id = 'distance'
        # bmi_calculator
        self.height_units_id = 'height_units'
        self.height_id = 'height'
        self.weight_id = 'weight'
        self.bmi_result = 'div.fieldLabel > span:nth-child(1)'
        self.bmi_message = 'div.fieldLabel > span:nth-child(2)'
        # probable_result_calculator
        self.time_id = 'time'
        self.mile_result_css = 'div.formGroupWrapper > div:nth-child(3) > div.fieldLabel'
        # running_pace_calculator
        self.pace_id = 'pace'
        self.time_css = 'div.formGroupWrapper > div:nth-child(4) > div.fieldLabel'

    def turning_off_the_banner(self):
        self.logger.info('Turning off the banner.')
        banner = self.driver.find_element_by_css_selector(self.banner_css)
        if banner.is_enabled():
            self.driver.find_element_by_css_selector(self.banner_accept_css).click()
        else:
            print('Banner is not displayed.')

    def set_bmi_calculator(self, height, weight):
        self.logger.info('Setting calculator with: {}, {}'.format(height, weight))
        select = Select(self.driver.find_element_by_id(self.height_units_id))
        select.select_by_index(1)
        self.driver.find_element_by_id(self.height_id).send_keys(height)
        self.driver.find_element_by_id(self.weight_id).send_keys(weight)
        self.driver.find_element_by_css_selector(self.btn_calculate_css).click()

    def get_bmi_page_results(self):
        self.logger.info('Getting bmi page results:')
        page_bmi = self.driver.find_element_by_css_selector(self.bmi_result).text
        page_message = self.driver.find_element_by_css_selector(self.bmi_message).text
        self.logger.info('{}, {}'.format(page_bmi, page_message))
        return page_bmi, page_message

    def set_probable_result_calculator(self, seconds):
        self.logger.info('Setting probable result calculator with: {}'.format(seconds))
        select = Select(self.driver.find_element_by_id(self.distance_id))
        select.select_by_index(1)
        hhmmss = formulas.seconds_to_hhmmss(seconds)
        self.driver.find_element_by_id(self.time_id).send_keys(' ' + hhmmss)
        self.driver.find_element_by_css_selector(self.btn_calculate_css).click()

    def get_probable_page_result(self):
        self.logger.info('Getting probable result page result:')
        one_mile = self.driver.find_element_by_css_selector(self.mile_result_css).text
        self.logger.info(one_mile)
        return one_mile

    def set_running_pace_calculator(self, distance, pace):
        self.logger.info('Setting running pace calculator with: {}, {}'.format(distance, pace))
        self.driver.find_element_by_id(self.distance_id).send_keys(distance)
        hhmmss = formulas.seconds_to_hhmmss(pace)
        hhmmss = str(hhmmss).replace('00:', '')
        self.driver.find_element_by_id(self.pace_id).send_keys(' ' + hhmmss)
        self.driver.find_element_by_css_selector(self.btn_calculate_css).click()

    def get_running_pace_calculator_result(self):
        self.logger.info('Getting running pace calculator result:')
        time = self.driver.find_element_by_css_selector(self.time_css).text
        self.logger.info(time)
        return time
