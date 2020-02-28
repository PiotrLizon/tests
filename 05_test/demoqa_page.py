import logging
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver


class DemoqaPage:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.drag_id = 'draggable'
        self.drop_id = 'droppable'
        self.box_css = 'div.ui-droppable p'
        self.btn_link_text = 'Tooltip and Double click'
        self.dbl_btn_id = 'doubleClickBtn'
        self.right_click_btn_id = 'rightClickBtn'
        self.item_xpath = '//*[@id="rightclickItem"]/div[1]'
        self.hover_id = 'tooltipDemo'
        self.hover_class = 'tooltiptext'

    @allure.step('Dragging and dropping.')
    def drag_and_drop(self):
        self.logger.info('Dragging and dropping.')
        draggable = self.driver.find_element_by_id(self.drag_id)
        droppable = self.driver.find_element_by_id(self.drop_id)
        webdriver.ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()
        allure.attach(self.driver.get_screenshot_as_png(name='drag_drop', attachment_type=AttachmentType.PNG))

    @allure.step('Getting result.')
    def get_result(self):
        self.logger.info('Getting result:')
        result = self.driver.find_element_by_css_selector(self.box_css).text
        self.logger.info(result)
        allure.attach(self.driver.get_screenshot_as_png(name='get_result', attachment_type=AttachmentType.PNG))
        return result

    @allure.step('Going to new tab.')
    def switch_to_tooltip_and_double_click(self):
        self.logger.info('Going to new tab.')
        self.driver.find_element_by_link_text(self.btn_link_text).click()

    @allure.step('Double clicking.')
    def double_click(self):
        self.logger.info('Double clicking:')
        button = self.driver.find_element_by_id(self.dbl_btn_id)
        webdriver.ActionChains(self.driver).double_click(button).perform()
        alert_text = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.logger.info(alert_text)
        allure.attach(self.driver.get_screenshot_as_png(name='double_click', attachment_type=AttachmentType.PNG))
        return alert_text

    @allure.step('Right clicking.')
    def right_click(self):
        self.logger.info("Right clicking:")
        button = self.driver.find_element_by_id(self.right_click_btn_id)
        webdriver.ActionChains(self.driver).context_click(button).perform()
        self.driver.find_element_by_xpath(self.item_xpath).click()
        alert_text_two = self.driver.switch_to.alert.text
        self.driver.switch_to.alert.accept()
        self.logger.info(alert_text_two)
        allure.attach(self.driver.get_screenshot_as_png(name='right_click', attachment_type=AttachmentType.PNG))
        return alert_text_two

    @allure.step('Hover.')
    def hover(self):
        self.logger.info('Hover:')
        element = self.driver.find_element_by_id(self.hover_id)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        text = self.driver.find_element_by_class_name(self.hover_class).text
        self.logger.info(text)
        allure.attach(self.driver.get_screenshot_as_png(name='right_click', attachment_type=AttachmentType.PNG))
        return text
