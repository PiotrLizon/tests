import math


# CUBE
def cube_surface(a):
    # a - side
    return str(round(6 * a ** 2, 2))


def cube_volume(a):
    # a - side
    return str(round(a ** 3, 2))


# CUBOID
def cuboid_surface(a, b, c):
    # a, b, c - sides
    return str(round(2 * (a * b + a * c + b * c), 2))


def cuboid_volume(a, b, c):
    # a, b, c - sides
    return str(round(a * b * c, 2))


# CYLINDER
def cylinder_surface(r, h):
    # r - radius
    # h - height
    return str(round(2 * math.pi * r * (r + h), 2))


def cylinder_volume(r, h):
    # r - radius
    # h - height
    return str(round(math.pi * r ** 2 * h, 2))


# CONE
def cone_surface(r, s):
    # s - generatrix cone
    # r - radius
    return str(round(math.pi * r * (r + s), 2))


def cone_volume(r, h):
    # r - radius
    # h - height
    return str(round(1 / 3 * math.pi * r ** 2 * h, 2))


# SPHERE
def sphere_surface(r):
    # r - radius
    return str(round(4 * math.pi * r ** 2, 2))


def sphere_volume(r):
    # r - radius
    return str(round(4 / 3 * math.pi * r ** 3, 2))


# PRISM
def base_prism_surface(n, a):
    # n - number of sides
    # a - side
    return 1 / 4 * n * a ** 2 * (1 / math.tan(math.pi / n))


def lateral_prism_surface(n, a, h):
    # n - number of sides
    # a - side
    # h - height
    return round(n * a * h, 2)


def prism_surface(x, y):
    # x - base prism surface
    # y - lateral prism surface
    return str(round(2 * x + y, 2))


def prism_volume(x, h):
    # x - base prism surface
    # h - height
    return str(round(x * h, 2))
