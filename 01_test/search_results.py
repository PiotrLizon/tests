import logging
import allure
from allure_commons.types import AttachmentType


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.heading_selector = 'div.g-col-8 div span.h3.u-text-break-word'
        self.price_selector = 'div.price-block span.h3.u-block'

    @allure.step('Checking results')
    def get_headings(self):
        headings = self.driver.find_elements_by_css_selector(self.heading_selector)
        heading_values = [heading.get_attribute('textContent') for heading in headings]
        self.logger.info('Headings are:')
        allure.attach(self.driver.get_screenshot_as_png(), name='get_headings', attachment_type=AttachmentType.PNG)
        for heading in heading_values:
            self.logger.info(heading)
        return heading_values

    def get_prices(self):
        prices = self.driver.find_elements_by_css_selector(self.price_selector)
        price_values = [price.get_attribute('textContent') for price in prices]
        price_values_2 = [price.replace('€', ' ') for price in price_values]
        price_values_3 = [int(price.replace('.', '')) for price in price_values_2]
        self.logger.info('Prices are:')
        for price in price_values_3:
            self.logger.info(price)
        return price_values_3

