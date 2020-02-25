import allure
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from phptravels_page import PhptravelsPage


class TestContactForm:

    @allure.title('Contact form test.')
    @allure.description('testing complaint submission by the user.')
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_page(self, setup):
        self.driver.get('https://www.phptravels.net/home')
        php_travels_page = PhptravelsPage(self.driver)
        php_travels_page.log_in('user@phptravels.com', 'demouser')
        welcome = php_travels_page.get_welcome_message()
        assert welcome == 'Hi, Demo User', 'failed'
        php_travels_page.open_the_form()
        contact_title = php_travels_page.get_contact_page_title()
        assert contact_title == 'Contact Us', 'failed'
        php_travels_page.fill_out_the_form('Oscar Martinez', 'oscar.martinez@xxx.com',
                                           'accommodation', 'message')
        alert = php_travels_page.get_the_alert()
        assert alert == 'Please Verify Recaptcha', 'failed'
