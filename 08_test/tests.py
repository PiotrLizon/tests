import pytest
import results
from page import Page
import data

values = data.get_setup_data()


class Test:

    @pytest.fixture()
    def setup(self):
        self.driver = data.get_driver(values[3])
        self.driver.implicitly_wait(values[1])
        self.driver.maximize_window()
        self.driver.get(values[2])
        yield
        self.driver.quit()

    def test_cube(self, setup):
        cube = data.get_data()
        page = Page(self.driver)
        page.set_cube(cube[0][1])
        page_results = page.get_page_results()
        correct_results = results.get_cube_results(cube[0][0])
        assert page_results[0] == correct_results[0], values[0]
        assert page_results[1] == correct_results[1], values[0]

    def test_cuboid(self, setup):
        cuboid = data.get_data()
        page = Page(self.driver)
        page.set_cuboid(cuboid[1][1], cuboid[1][3], cuboid[1][5])
        page_results = page.get_page_results()
        correct_results = results.get_cuboid_results(cuboid[1][0], cuboid[1][2], cuboid[1][4])
        assert page_results[0] == correct_results[0], values[0]
        assert page_results[1] == correct_results[1], values[0]

    def test_cylinder(self, setup):
        cylinder = data.get_data()
        page = Page(self.driver)
        page.set_cylinder(cylinder[2][1], cylinder[2][3])
        page_results = page.get_page_results()
        correct_results = results.get_cylinder_results(cylinder[2][0], cylinder[2][2])
        assert page_results[0] == correct_results[0], values[0]
        assert page_results[1] == correct_results[1], values[0]

    def test_cone(self, setup):
        cone = data.get_data()
        page = Page(self.driver)
        page.set_cone(cone[3][1], cone[3][3], cone[3][5])
        page_results = page.get_page_results()
        correct_results = results.get_cone_results(cone[3][0], cone[3][2], cone[3][4])
        assert page_results[0] == correct_results[0], values[0]
        assert page_results[1] == correct_results[1], values[0]

    def test_sphere(self, setup):
        sphere = data.get_data()
        page = Page(self.driver)
        page.set_sphere(sphere[4][1])
        page_results = page.get_page_results()
        correct_results = results.get_sphere_results(sphere[4][0])
        assert page_results[0] == correct_results[0], values[0]
        assert page_results[1] == correct_results[1], values[0]

    def test_prism(self, setup):
        prism = data.get_data()
        page = Page(self.driver)
        page.set_prism(prism[5][1], prism[5][3], prism[5][5])
        page_results = [page.get_base_lateral_prism_results(), page.get_page_results()]
        correct_results = results.get_prism_results(prism[5][0], prism[5][2], prism[5][4])
        assert page_results[0][0] == correct_results[0], values[0]
        assert page_results[0][1] == correct_results[1], values[0]
        assert page_results[1][0] == correct_results[2], values[0]
        assert page_results[1][1] == correct_results[3], values[0]
