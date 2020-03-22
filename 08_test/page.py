import logging
from selenium.webdriver.common.keys import Keys


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.attribute_value = 'value'
        self.volume_name = 'objem'
        self.surface_name = 'povrch'
        self.base_name = 'povrchP'
        self.lateral_name = 'povrchPl'
        self.side_name = 'strana'
        self.radius_name = 'polomer'
        self.height_name = 'vyska'
        # cube
        self.cube_link = 'Sześcian'
        # cuboid
        self.cuboid_link = 'Prostopadłościan'
        self.side_a_name = 'stranaA'
        self.side_b_name = 'stranaB'
        self.side_c_name = 'stranaC'
        # cylinder
        self.cylinder_link = 'Walec'
        # cone
        self.cone_link = 'Stożek'
        self.s_height_name = 'vyskaS'
        # sphere
        self.sphere_link = 'Kula'
        # prism
        self.prism_link = 'Graniastosłup'
        self.n_sides_name = 'pocet'

    def get_page_results(self):
        self.logger.info('Getting page results:')
        volume = self.driver.find_element_by_name(self.volume_name).get_attribute(self.attribute_value)
        surface = self.driver.find_element_by_name(self.surface_name).get_attribute(self.attribute_value)
        self.logger.info('{}, {}'.format(volume, surface))
        return volume, surface

    def get_base_lateral_prism_results(self):
        self.logger.info('Getting page results:')
        base = self.driver.find_element_by_name(self.base_name).get_attribute(self.attribute_value)
        lateral = self.driver.find_element_by_name(self.lateral_name).get_attribute(self.attribute_value)
        self.logger.info('{}, {}'.format(base, lateral))
        return base, lateral

    def set_cube(self, a):
        self.logger.info('Setting cube with: {}'.format(a))
        self.driver.find_element_by_link_text(self.cube_link).click()
        self.driver.find_element_by_name(self.side_name).send_keys(a, Keys.ENTER)

    def set_cuboid(self, a, b, c):
        self.logger.info('Setting cuboid with: {}, {}, {}'.format(a, b, c))
        self.driver.find_element_by_link_text(self.cuboid_link).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_b_name).send_keys(b)
        self.driver.find_element_by_name(self.side_c_name).send_keys(c, Keys.ENTER)

    def set_cylinder(self, r, h):
        self.logger.info('Setting cylinder with: {}, {}'.format(r, h))
        self.driver.find_element_by_link_text(self.cylinder_link).click()
        self.driver.find_element_by_name(self.radius_name).send_keys(r)
        self.driver.find_element_by_name(self.height_name).send_keys(h, Keys.ENTER)

    def set_cone(self, h, s, r):
        self.logger.info('Setting cone with: {}, {}, {}'.format(h, s, r))
        self.driver.find_element_by_link_text(self.cone_link).click()
        self.driver.find_element_by_name(self.height_name).send_keys(h)
        self.driver.find_element_by_name(self.s_height_name).send_keys(s)
        self.driver.find_element_by_name(self.radius_name).send_keys(r, Keys.ENTER)

    def set_sphere(self, r):
        self.logger.info('Setting sphere with: {}'.format(r))
        self.driver.find_element_by_link_text(self.sphere_link).click()
        self.driver.find_element_by_name(self.radius_name).send_keys(r, Keys.ENTER)

    def set_prism(self, n, a, h):
        self.logger.info('Setting prism with: {}, {}, {}'.format(n, a, h))
        self.driver.find_element_by_link_text(self.prism_link).click()
        self.driver.find_element_by_name(self.n_sides_name).send_keys(n)
        self.driver.find_element_by_name(self.side_name).send_keys(a)
        self.driver.find_element_by_name(self.height_name).send_keys(h, Keys.ENTER)
