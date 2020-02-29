import logging
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class BiegnijmyPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.calculator_names_xpath = ['//*[@id="TRESC"]/h1[2]', '//*[@id="TRESC"]/h1[3]',
                                       '//*[@id="TRESC"]/h1[4]', '//*[@id="TRESC"]/h1[5]']
        self.calculator_names = ['KALKULATOR TEMPA BIEGU', 'KALKULATOR CZASU ODCINKA',
                                 'KALKULATOR DŁUGOŚCI KROKU', 'KALKULATOR ODLEGŁOŚCI']
        self.select_distance_name = 'dystanswybor'
        self.minutes_name = 'minuty'
        self.btn_peace_xpath = '//*[@id="TRESC"]/form[1]/p[3]/input'
        self.peace_value_name = 'ans'
        self.speed_value_name = 'ans2'
        self.attribute = 'value'
        self.episode_time_name = 'tempomin'
        self.episode_distance_name = 'odcinekm'
        self.btn_distance_xpath = '//*[@id="TRESC"]/form[2]/p[3]/input'
        self.episode_time_value_name = 'ans3'
        self.stride_distance_name = 'odcinekmkrok'
        self.stride_name = 'ilosckrokow'
        self.btn_stride_xpath = '//*[@id="TRESC"]/form[3]/p[3]/input'
        self.stride_value_name = 'ans4'
        self.rate_input_name = 'otempomin'
        self.hours_input_name = 'ogodziny'
        self.minutes_input_name = 'ominuty'
        self.btn_xpath = '//*[@id="TRESC"]/form[4]/p[3]/input'
        self.distance_value_name = 'ans5'

    @staticmethod
    def set_driver(driver):
        if driver == 'chrome':
            return webdriver.Chrome(ChromeDriverManager().install())
        elif driver == 'firefox':
            return webdriver.Firefox(executable_path=GeckoDriverManager().install())
        raise Exception('Provide valid driver name.')

    def get_and_check_titles(self):
        self.logger.info('Getting and checking titles:')
        titles = []
        for i in range(len(self.calculator_names_xpath)):
            h1 = self.driver.find_element_by_xpath(self.calculator_names_xpath[i]).text
            titles.append(h1)
        self.logger.info(titles)
        results = []
        for j in range(len(self.calculator_names_xpath)):
            if titles[j] == self.calculator_names[j]:
                result = True
                results.append(result)
            elif titles[j] != self.calculator_names[j]:
                result = False
                results.append(result)
        self.logger.info(results)
        return results

    @allure.step('Setting running peace: {1}, {2}')
    def set_running_peace_calculator(self, distance, minute):
        self.logger.info('Setting running peace: {}, {}'.format(distance, minute))
        select = Select(self.driver.find_element_by_name(self.select_distance_name))
        select.select_by_visible_text(distance)
        minutes = self.driver.find_element_by_name(self.minutes_name)
        minutes.clear()
        minutes.send_keys(minute)
        allure.attach(self.driver.get_screenshot_as_png(name="set_running_peace", attachment_type=AttachmentType.PNG))
        self.driver.find_element_by_xpath(self.btn_peace_xpath).click()

    def get_running_peace_result(self):
        self.logger.info('Getting running peace result.')
        peace = self.driver.find_element_by_name(self.peace_value_name).get_attribute(self.attribute)
        speed = self.driver.find_element_by_name(self.speed_value_name).get_attribute(self.attribute)
        return peace, speed

    @allure.step('Setting episode time with: {1} and {2}')
    def set_episode_time_calculator(self, rate, distance):
        self.logger.info('Setting episode time with: {} and {}'.format(rate, distance))
        time = self.driver.find_element_by_name(self.episode_time_name)
        time.click()
        time.send_keys(rate)
        episode = self.driver.find_element_by_name(self.episode_distance_name)
        episode.clear()
        episode.send_keys(distance)
        allure.attach(self.driver.get_screenshot_as_png(name="episode_time", attachment_type=AttachmentType.PNG))
        self.driver.find_element_by_xpath(self.btn_distance_xpath).click()

    def get_episode_time_result(self):
        self.logger.info('Getting episode time result:')
        episode_time = self.driver.find_element_by_name(self.episode_time_value_name).get_attribute(self.attribute)
        self.logger.info(episode_time)
        return episode_time

    @allure.step('Setting stride length: {1}, {2}')
    def set_stride_length_calculator(self, distance_, steps):
        self.logger.info('Setting stride length: {}, {}'.format(distance_, steps))
        distance = self.driver.find_element_by_name(self.stride_distance_name)
        distance.clear()
        distance.send_keys(distance_)
        number_of_steps = self.driver.find_element_by_name(self.stride_name)
        number_of_steps.clear()
        number_of_steps.send_keys(steps)
        allure.attach(self.driver.get_screenshot_as_png(name="stride_length", attachment_type=AttachmentType.PNG))
        self.driver.find_element_by_xpath(self.btn_stride_xpath).click()

    def get_stride_length_result(self):
        self.logger.info('Getting stride length:')
        stride_length = self.driver.find_element_by_name(self.stride_value_name).get_attribute(self.attribute)
        self.logger.info(stride_length)
        return stride_length

    @allure.step('Setting distance with: {1}, {2}, {3}')
    def set_distance_calculator(self, rate_, hours, minutes):
        self.logger.info('Setting distance with: {}, {}, {}'.format(rate_, hours, minutes))
        rate = self.driver.find_element_by_name(self.rate_input_name)
        rate.clear()
        rate.send_keys(rate_)
        time_hours = self.driver.find_element_by_name(self.hours_input_name)
        time_hours.clear()
        time_hours.send_keys(hours)
        time_minutes = self.driver.find_element_by_name(self.minutes_input_name)
        time_minutes.clear()
        time_minutes.send_keys(minutes)
        allure.attach(self.driver.get_screenshot_as_png(name="distance", attachment_type=AttachmentType.PNG))
        self.driver.find_element_by_xpath(self.btn_xpath).click()

    def get_distance_result(self):
        self.logger.info('Getting distance:')
        distance = self.driver.find_element_by_name(self.distance_value_name).get_attribute(self.attribute)
        self.logger.info(distance)
        return distance

