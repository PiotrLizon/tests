import allure
import pytest
from conftest import MainTest
from demoqa_page import DemoqaPage


@pytest.mark.usefixtures('setup')
class TestDemoqaPage(MainTest):

    @allure.title('Test')
    @allure.description('Test description.')
    def test(self, setup):
        demoqa_page = DemoqaPage(self.driver)
        demoqa_page.drag_and_drop()
        result = demoqa_page.get_result()
        assert result == 'Dropped!', 'failed'
        demoqa_page.switch_to_tooltip_and_double_click()
        alert_text = demoqa_page.double_click()
        assert 'Double Click Alert' in alert_text, 'failed'
        alert_text_two = demoqa_page.right_click()
        assert 'Edit' in alert_text_two
        text = demoqa_page.hover()
        assert text == 'We ask for your age only for statistical purposes.'
