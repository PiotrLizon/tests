import allure
import pytest
from pages.registration_page import RegistrationPage
from tests.conftest import MainTest


@pytest.mark.usefixtures('setup')
class TestRegistrationPage(MainTest):

    @allure.title('Automationpractice.com test')
    @allure.description('Automationpractice.com positive registration test')
    def test_registration_positive(self, setup):
        self.driver.get('http://automationpractice.com/index.php')
        registration_page = RegistrationPage(self.driver)
        registration_page.turning_on_the_form('xxx@xxx.xxx')
        registration_page.set_account_information('Jan', 'Kowalski', 'qwertyu')
        registration_page.set_the_date_of_birth('5', '10', '2000')
        registration_page.set_notifications()
        registration_page.set_account_address('ABC', 'Washington street 100', 'New York', 'New York', '00000')
        registration_page.set_the_phone_numbers('123456789', '987654321')
        assert 'Welcome to your account.' in registration_page.checking_positive_result()

    @allure.title('Automationpractice.com test')
    @allure.description('Automationpractice.com negative registration test')
    def test_registration_negative(self, setup):
        self.driver.get('http://automationpractice.com/index.php')
        registration_page = RegistrationPage(self.driver)
        registration_page.turning_on_the_form('xxx@xxx.xxx')
        registration_page.set_account_information('', '', 'qwertyu')
        registration_page.set_the_date_of_birth('5', '10', '2000')
        registration_page.set_notifications()
        registration_page.set_account_address('ABC', 'Washington street 100', 'New York', 'New York', '00000')
        registration_page.set_the_phone_numbers('zxcv', 'vcxz')
        assert 'There are 4 errors' == registration_page.checking_negative_result()
