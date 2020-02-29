import allure
import pytest
from page_object_pattern.page.biegnijmy_page import BiegnijmyPage
from page_object_pattern.conftest import MainTest


@pytest.mark.usefixtures('setup')
class TestBiegnijmy(MainTest):

    @allure.title('Test')
    @allure.description('Test calculators title')
    def test_calculators_title(self, setup):
        page = BiegnijmyPage(self.driver)
        results = page.get_and_check_titles()
        for i in range(len(results)):
            assert results[i], 'failed'

    @allure.title('Test')
    @allure.description('Test running peace calculator')
    def test_running_peace_calculator(self, setup):
        page = BiegnijmyPage(self.driver)
        page.set_running_peace_calculator('10 km', '50')
        peace_and_speed = page.get_running_peace_result()
        assert '5' in peace_and_speed[0], 'failed'
        assert '12' in peace_and_speed[1], 'failed'

    @allure.title('Test')
    @allure.description('Test episode time calculator')
    def test_episode_time_calculator(self, setup):
        page = BiegnijmyPage(self.driver)
        page.set_episode_time_calculator('5', '10000')
        episode_time = page.get_episode_time_result()
        assert '50' in episode_time, 'failed'

    @allure.title('Test')
    @allure.description('Test stride length calculator')
    def test_stride_length_calculator(self, setup):
        page = BiegnijmyPage(self.driver)
        page.set_stride_length_calculator('10000', '15000')
        stride_length = page.get_stride_length_result()
        assert '67' in stride_length

    @allure.title('Test')
    @allure.description('Test distance calculator')
    def test_distance_calculator(self):
        page = BiegnijmyPage(self.driver)
        page.set_distance_calculator('5', '1', '30')
        distance = page.get_distance_result()
        assert '18' in distance

