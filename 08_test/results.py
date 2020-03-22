import logging
import formulas

logger = logging.getLogger(__name__)


def get_cube_results(a):
    logger.info('Getting correct cube results:')
    volume = formulas.cube_volume(a)
    volume = volume.replace('.', ',')
    surface = formulas.cube_surface(a)
    surface = surface.replace('.', ',')
    logger.info('{}, {}'.format(volume, surface))
    return volume, surface


def get_cuboid_results(a, b, c):
    logger.info('Getting correct cuboid results:')
    volume = formulas.cuboid_volume(a, b, c)
    volume = volume.replace('.', ',')
    surface = formulas.cuboid_surface(a, b, c)
    surface = surface.replace('.', ',')
    logger.info('{}, {}'.format(volume, surface))
    return volume, surface


def get_cylinder_results(r, h):
    logger.info('Getting correct cylinder results:')
    volume = formulas.cylinder_volume(r, h)
    volume = volume.replace('.', ',')
    surface = formulas.cylinder_surface(r, h)
    surface = surface.replace('.', ',')
    logger.info('{}, {}'.format(volume, surface))
    return volume, surface


def get_cone_results(h, s, r):
    logger.info('Getting correct cone results:')
    volume = formulas.cone_volume(r, h)
    volume = volume.replace('.', ',')
    surface = formulas.cone_surface(r, s)
    surface = surface.replace('.', ',')
    logger.info('{}, {}'.format(volume, surface))
    return volume, surface


def get_sphere_results(r):
    logger.info('Getting correct sphere results:')
    volume = formulas.sphere_volume(r)
    volume = volume.replace('.', ',')
    surface = formulas.sphere_surface(r)
    surface = surface.replace('.', ',')
    logger.info('{}, {}'.format(volume, surface))
    return volume, surface


def get_prism_results(n, a, h):
    logger.info('Getting correct prism results:')
    base = formulas.base_prism_surface(n, a)
    round_base = round(formulas.base_prism_surface(n, a), 2)
    lateral = formulas.lateral_prism_surface(n, a, h)
    volume = formulas.prism_volume(base, h)
    volume = volume.replace('.', ',')
    surface = formulas.prism_surface(round_base, lateral)
    surface = surface.replace('.', ',')
    logger.info('{}, {}, {}, {}'.format(round_base, lateral, volume, surface))
    return str(round_base).replace('.', ','), str(lateral).replace('.', ','), volume, surface
