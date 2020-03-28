import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import formulas
from page import Page


class Tests:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()

    def test_bmi_calculator(self, setup):
        self.driver.get('https://www.runners-world.pl/kalkulatory-biegowe/bmi,9668,1')
        page = Page(self.driver)
        page.turning_off_the_banner()
        page.set_bmi_calculator('1.55', '35')
        page_results = page.get_bmi_page_results()
        expected_results = formulas.get_bmi_expected_results(1.55, 35)
        assert page_results[0] == expected_results[0], 'Assertion failed'
        assert page_results[1] == expected_results[1], 'Assertion failed'

    def test_probable_result_calculator(self, setup):
        self.driver.get('https://www.runners-world.pl/kalkulatory-biegowe/prognoza-wynikow,9663,1')
        page = Page(self.driver)
        page.turning_off_the_banner()
        page.set_probable_result_calculator(243)
        page_result = page.get_probable_page_result()
        expected_result = formulas.get_probable_result_expected_result(243)
        assert page_result == expected_result, 'Assertion failed'

    def test_running_pace_calculator(self, setup):
        self.driver.get('https://www.runners-world.pl/kalkulatory-biegowe/tempo-biegu,9665,1')
        page = Page(self.driver)
        page.turning_off_the_banner()
        page.set_running_pace_calculator('12.5', 276)
        page_result = page.get_running_pace_calculator_result()
        expected_result = formulas.get_expected_running_pace_calculator_result('12.5', 276)
        assert page_result == expected_result, 'Assertion failed'
