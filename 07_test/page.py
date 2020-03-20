import logging
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.logger = logging.getLogger(__name__)
        self.input_value = 'value'
        self.field_name = 'obsah'
        self.circumference_name = 'obvod'
        self.side_name = 'strana'
        self.side_a_name = 'stranaA'
        self.side_b_name = 'stranaB'
        self.side_c_name = 'stranaC'
        self.height_name = 'vyska'
        # circle
        self.circle_link_text = 'Koło'
        self.circle_radius_name = 'polomer'
        self.circle_diameter_name = 'prumer'
        # triangle
        self.triangle_link_text = 'Trójkąt'
        self.triangle_unit_name = 'jednotkaU'
        self.triangle_angle_name = 'beta'
        # rectangular triangle
        self.rectangular_triangle_link_text = 'Trójkąt prostokątny'
        # square
        self.square_link_text = 'Kwadrat'
        # rectangle
        self.rectangle_link_text = 'Prostokąt'
        # rhombus
        self.rhombus_link_text = 'Romb'
        # parallelogram
        self.parallelogram_link_text = 'Równoległobok'
        self.parallelogram_height_name = 'vyskaA'
        # trapeze
        self.trapeze_link_text = 'Trapez'
        # pentagon
        self.pentagon_link_text = 'Pięciokąt foremny'
        self.pentagon_radius_name = 'polomerO'
        # hexagon
        self.hexagon_link_text = 'Sześciokąt foremny'
        # polygon
        self.polygon_link_text = 'Wielokąt foremny'
        self.polygon_n_name = 'en'
        # pythagorean theorem
        self.pythagorean_theorem_link_text = 'Twierdzenie Pitagorasa'

    def get_page_results(self):
        self.logger.info('Getting page results:')
        field = self.driver.find_element_by_name(self.field_name).get_attribute(self.input_value)
        circumference = self.driver.find_element_by_name(self.circumference_name).get_attribute(self.input_value)
        self.logger.info('{}, {}'.format(field, circumference))
        return field, circumference

    def get_page_result(self):
        self.logger.info('Getting page result.')
        field = self.driver.find_element_by_name(self.field_name).get_attribute(self.input_value)
        self.logger.info(field)
        return field

    def get_page_pythagorean_theorem_result(self):
        self.logger.info('Getting page result.')
        side = self.driver.find_element_by_name(self.side_c_name).get_attribute(self.input_value)
        self.logger.info(side)
        return side

    def circle(self, r, d):
        self.logger.info('Setting circle: {}, {}'.format(r, d))
        self.driver.find_element_by_link_text(self.circle_link_text).click()
        self.driver.find_element_by_name(self.circle_radius_name).send_keys(r)
        self.driver.find_element_by_name(self.circle_diameter_name).send_keys(d, Keys.ENTER)

    def triangle(self, a, b, c, x):
        self.logger.info('Setting triangle: {}, {}, {}, {}'.format(a, b, c, x))
        self.driver.find_element_by_link_text(self.triangle_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_b_name).send_keys(b)
        self.driver.find_element_by_name(self.side_c_name).send_keys(c)
        select_value = Select(self.driver.find_element_by_name(self.triangle_unit_name))
        select_value.select_by_index(1)
        self.driver.find_element_by_name(self.triangle_angle_name).send_keys(x, Keys.ENTER)

    def rectangular_triangle(self, a, b, c):
        self.logger.info('Setting circle: {}, {}, {}'.format(a, b, c))
        self.driver.find_element_by_link_text(self.rectangular_triangle_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_b_name).send_keys(b)
        self.driver.find_element_by_name(self.side_c_name).send_keys(c, Keys.ENTER)

    def square(self, a):
        self.logger.info('Setting square: {}'.format(a))
        self.driver.find_element_by_link_text(self.square_link_text).click()
        self.driver.find_element_by_name(self.side_name).send_keys(a, Keys.ENTER)

    def rectangle(self, a, b):
        self.logger.info('Setting rectangle: {}, {}'.format(a, b))
        self.driver.find_element_by_link_text(self.rectangle_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_b_name).send_keys(b, Keys.ENTER)

    def rhombus(self, a, h):
        self.logger.info('Setting rhombus: {}, {}'.format(a, h))
        self.driver.find_element_by_link_text(self.rhombus_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.height_name).send_keys(h, Keys.ENTER)

    def parallelogram(self, a, b, h):
        self.logger.info('Setting parallelogram: {}, {}, {}'.format(a, b, h))
        self.driver.find_element_by_link_text(self.parallelogram_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_b_name).send_keys(b)
        self.driver.find_element_by_name(self.parallelogram_height_name).send_keys(h, Keys.ENTER)

    def trapeze(self, a, c, h):
        self.logger.info('Setting trapeze: {}, {}, {}'.format(a, c, h))
        self.driver.find_element_by_link_text(self.trapeze_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_c_name).send_keys(c)
        self.driver.find_element_by_name(self.height_name).send_keys(h, Keys.ENTER)

    def pentagon(self, a):
        self.logger.info('Setting pentagon: {}'.format(a))
        self.driver.find_element_by_link_text(self.pentagon_link_text).click()
        self.driver.find_element_by_name(self.side_name).send_keys(a)
        self.driver.find_element_by_name(self.pentagon_radius_name).send_keys(Keys.ENTER)

    def hexagon(self, a):
        self.logger.info('Setting hexagon: {}'.format(a))
        self.driver.find_element_by_link_text(self.hexagon_link_text).click()
        self.driver.find_element_by_name(self.side_name).send_keys(a, Keys.ENTER)

    def polygon(self, n, a):
        self.logger.info('Setting polygon: {}, {}'.format(n, a))
        self.driver.find_element_by_link_text(self.polygon_link_text).click()
        self.driver.find_element_by_name(self.polygon_n_name).send_keys(n)
        self.driver.find_element_by_name(self.side_name).send_keys(a, Keys.ENTER)

    def pythagorean_theorem(self, a, b):
        self.logger.info('Setting pythagorean theorem: {}, {}'.format(a, b))
        self.driver.find_element_by_link_text(self.pythagorean_theorem_link_text).click()
        self.driver.find_element_by_name(self.side_a_name).send_keys(a)
        self.driver.find_element_by_name(self.side_b_name).send_keys(b, Keys.ENTER)
