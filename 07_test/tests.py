import pytest
from pages.page import Page
import pages.results
from pages.data import Data


class Tests:

    @pytest.fixture()
    def setup(self):
        setup_data = Data.setup_data()
        self.driver = Data.get_driver(setup_data[1][0])
        self.driver.maximize_window()
        self.driver.implicitly_wait(setup_data[2])
        self.driver.get(setup_data[3])
        yield
        self.driver.quit()

    def test_circle(self, setup):
        circle = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.circle(circle[0][1], circle[0][3])
        results = page.get_page_results()
        expected_results = pages.results.get_circle_results(circle[0][0], circle[0][2])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_triangle(self, setup):
        triangle = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.triangle(triangle[1][1], triangle[1][3], triangle[1][5], triangle[1][7])
        results = page.get_page_results()
        expected_results = pages.results.get_triangle_results(triangle[1][0],
                                                              triangle[1][2],
                                                              triangle[1][4],
                                                              triangle[1][6])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_rectangular_triangle(self, setup):
        rectangular_triangle = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.rectangular_triangle(rectangular_triangle[2][1], rectangular_triangle[2][3], rectangular_triangle[2][5])
        results = page.get_page_results()
        expected_results = pages.results.get_rectangular_triangle_results(rectangular_triangle[2][0],
                                                                          rectangular_triangle[2][2],
                                                                          rectangular_triangle[2][4])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_square(self, setup):
        square = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.square(square[3][1])
        results = page.get_page_results()
        expected_results = pages.results.get_square_results(square[3][0])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_rectangle(self, setup):
        rectangle = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.rectangle(rectangle[4][1], rectangle[4][3])
        results = page.get_page_results()
        expected_results = pages.results.get_rectangle_results(rectangle[4][0], rectangle[4][2])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_rhombus(self, setup):
        rhombus = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.rhombus(rhombus[5][1], rhombus[5][3])
        results = page.get_page_results()
        expected_results = pages.results.get_rhombus_results(rhombus[5][0], rhombus[5][2])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_parallelogram(self, setup):
        parallelogram = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.parallelogram(parallelogram[6][1], parallelogram[6][3], parallelogram[6][5])
        results = page.get_page_results()
        expected_results = pages.results.get_parallelogram_results(parallelogram[6][0],
                                                                   parallelogram[6][2],
                                                                   parallelogram[6][4])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_trapeze(self, setup):
        trapeze = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.trapeze(trapeze[7][1], trapeze[7][3], trapeze[7][5])
        result = page.get_page_result()
        expected_result = pages.results.get_trapeze_results(trapeze[7][0],
                                                            trapeze[7][2],
                                                            trapeze[7][4])
        assert result[0] == expected_result[0], message[0]

    def test_pentagon(self, setup):
        pentagon = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.pentagon(pentagon[8][1])
        results = page.get_page_results()
        expected_results = pages.results.get_pentagon_results(pentagon[8][0])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_hexagon(self, setup):
        hexagon = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.hexagon(hexagon[9][1])
        results = page.get_page_results()
        expected_results = pages.results.get_hexagon_results(hexagon[9][0])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_polygon(self, setup):
        polygon = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.polygon(polygon[10][1], polygon[10][3])
        results = page.get_page_results()
        expected_results = pages.results.get_polygon_results(polygon[10][0], polygon[10][2])
        assert results[0] == expected_results[0], message[0]
        assert results[1] == expected_results[1], message[0]

    def test_pythagorean_theorem(self, setup):
        pythagorean_theorem = Data.get_data()
        message = Data.setup_data()
        page = Page(self.driver)
        page.pythagorean_theorem(pythagorean_theorem[11][1], pythagorean_theorem[11][3])
        result = page.get_page_pythagorean_theorem_result()
        expected_result = pages.results.get_pythagorean_theorem_result(pythagorean_theorem[11][0],
                                                                       pythagorean_theorem[11][2])
        assert result == expected_result, message[0]
