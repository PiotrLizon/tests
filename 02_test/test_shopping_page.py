import allure
import pytest
from pages.shopping_page import ShoppingPage
from tests.conftest import MainTest


@pytest.mark.usefixtures('setup')
class TestShoppingPage(MainTest):

    @allure.title('Automationpractice.com test')
    @allure.description('Automationpractice.com shopping page test')
    def test_shopping_page(self, setup):
        self.driver.get('http://automationpractice.com/index.php')
        shopping_page = ShoppingPage(self.driver)
        shopping_page.turning_on_the_store()
        shopping_page.adding_the_dress_to_cart()
        shopping_page.adding_a_different_size(2)
        results = (shopping_page.checking_the_order())
        assert 'S' in results[0]
        assert 'L' in results[1]
        assert 'Printed Dress' == results[2]
