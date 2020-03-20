import math


# CIRCLE
def circle_field(r):
    # r - radius
    return str(round(math.pi * r ** 2, 2))


def circumference_of_a_circle(d):
    # d - diameter
    return str(round(math.pi * d, 2))


# TRIANGLE
def triangle_field(a, c, x):
    # a - basis
    # h - height
    # x - beta angle between basis a and side c
    h = c * math.sin(x)
    return str(round((a * h) * 1 / 2, 2))


def circumference_of_a_triangle(a, b, c):
    # a, b, c - sides
    return str(round(a + b + c, 2))


# RECTANGULAR TRIANGLE
def rectangular_triangle_field(a, b):
    # a, b - sides
    return str(round(a * b * (1 / 2), 2))


def circumference_of_a_rectangular_triangle(a, b, c):
    # a, b, b - sides
    return str(round(a + b + c, 2))


# SQUARE
def square_field(a):
    # a - side
    return str(round(a ** 2, 2))


def circumference_of_a_square(a):
    # a - side
    return str(round(a * 4, 2))


# RECTANGLE
def rectangle_field(a, b):
    # a, b - sides
    return str(round(a * b, 2))


def circumference_of_a_rectangle(a, b):
    # a, b - sides
    return str(round((a + b) * 2, 2))


# RHOMBUS
def rhombus_field(a, h):
    # a - side
    # h - height
    return str(round(a * h, 2))


def circumference_of_a_rhombus(a):
    # a - side
    return str(round(a * 4, 2))


# PARALLELOGRAM
def parallelogram_field(a, h):
    # a - side
    # h - height
    return str(round(a * h, 2))


def circumference_of_a_parallelogram(a, b):
    # a, b - sides
    return str(round(2 * (a + b), 2))


# TRAPEZE
def trapeze_field(a, c, h):
    # a, c - basis
    # h - height
    return str(round((a + c) * h * (1 / 2), 2))


# PENTAGON
def pentagon_field(a):
    # a - side
    return str(round((math.sqrt(25 + 10 * math.sqrt(5)) * (1 / 4)) * a ** 2, 2))


def circumference_of_a_pentagon(a):
    # a - side
    return str(round(a * 5, 2))


# HEXAGON
def hexagon_field(a):
    # a - side
    return str(round((3 * math.sqrt(3) * (1 / 2)) * a ** 2, 2))


def circumference_of_a_hexagon(a):
    # a - side
    return str(round(a * 6, 2))


# POLYGON
def polygon_field(n, a):
    # a - side
    # n - amount of sides
    return str(round((1 / 4) * n * a ** 2 * (1 / math.tan(math.pi / n)), 2))


def circumference_of_a_polygon(n, a):
    # a - side
    # n - amount of sides
    return str(round(a * n, 2))


# PYTHAGOREAN THEOREM
def pythagorean_theorem(a, b):
    # a, b - sides
    return str(round(math.sqrt(a ** 2 + b ** 2), 2))
