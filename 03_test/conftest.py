import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class MainTest:

    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://redux-form.com/8.2.2/examples/fieldlevelvalidation/')
        yield
        self.driver.quit()
