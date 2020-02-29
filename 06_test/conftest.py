import pytest
from page_object_pattern.page.biegnijmy_page import BiegnijmyPage


class MainTest:

    @pytest.fixture()
    def setup(self):
        self.driver = BiegnijmyPage.set_driver('chrome')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get('http://biegnijmy.pl/kalkulator')
        yield
        self.driver.quit()

