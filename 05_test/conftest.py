import pytest
from driver_factory import DriverFactory


class MainTest:

    @pytest.fixture()
    def setup(self):
        self.driver = DriverFactory.get_driver('chrome')
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get('https://demoqa.com/droppable/')
        yield
        self.driver.quit()

