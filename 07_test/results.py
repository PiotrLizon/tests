import pages.formulas
import logging

logger = logging.getLogger(__name__)


def get_circle_results(r, d):
    logger.info('Getting circle results:')
    field = pages.formulas.circle_field(r)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_circle(d)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_triangle_results(a, b, c, x):
    logger.info('Getting triangle results:')
    field = pages.formulas.triangle_field(a, c, x)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_triangle(a, b, c)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_rectangular_triangle_results(a, b, c):
    logger.info('Getting rectangular triangle results:')
    field = pages.formulas.rectangular_triangle_field(a, b)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_rectangular_triangle(a, b, c)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_square_results(a):
    logger.info('Getting square results:')
    field = pages.formulas.square_field(a)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_square(a)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_rectangle_results(a, b):
    logger.info('Getting rectangle results:')
    field = pages.formulas.rectangle_field(a, b)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_rectangle(a, b)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_rhombus_results(a, h):
    logger.info('Getting rhombus results:')
    field = pages.formulas.rhombus_field(a, h)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_rhombus(a)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_parallelogram_results(a, b, h):
    logger.info('Getting parallelogram results:')
    field = pages.formulas.parallelogram_field(a, h)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_parallelogram(a, b)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_trapeze_results(a, c, h):
    logger.info('Getting trapeze result:')
    field = pages.formulas.trapeze_field(a, c, h)
    field = field.replace('.', ',')
    logger.info('{}'.format(field))
    return field


def get_pentagon_results(a):
    logger.info('Getting pentagon results:')
    field = pages.formulas.pentagon_field(a)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_pentagon(a)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_hexagon_results(a):
    logger.info('Getting hexagon results:')
    field = pages.formulas.hexagon_field(a)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_hexagon(a)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_polygon_results(n, a):
    logger.info('Getting polygon results:')
    field = pages.formulas.polygon_field(n, a)
    field = field.replace('.', ',')
    circumference = pages.formulas.circumference_of_a_polygon(n, a)
    circumference = circumference.replace('.', ',')
    logger.info('{}, {}'.format(field, circumference))
    return field, circumference


def get_pythagorean_theorem_result(a, b):
    logger.info('Getting pythagorean theorem result:')
    side = pages.formulas.pythagorean_theorem(a, b)
    side = side.replace('.', ',')
    logger.info('{}'.format(side))
    return side
