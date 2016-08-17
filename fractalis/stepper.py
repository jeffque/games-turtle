#!/bin/env python3

from .utils import size_inscrit_polygon

def triangle_fractal_stepper(size, new_size_deffer, tortuguita):
    step_size = new_size_deffer(size)
    yield 0
    tortuguita.forward(step_size)
    yield 1
    tortuguita.left(120)
    tortuguita.forward(step_size)
    tortuguita.left(-120)
    yield 2
    tortuguita.right(120)
    tortuguita.forward(step_size)
    tortuguita.right(-120)


def square_fractal_mid_stepper(size, new_size_deffer, tortuguita):
    step_size = (size - new_size_deffer(size)) / 2
    for x in range(0, 4):
        tortuguita.forward(step_size)
        tortuguita.right(90)
        yield x
        tortuguita.left(90)
        tortuguita.forward(size - step_size)
        tortuguita.left(90)


def square_fractal_corner_stepper(size, new_size_deffer, tortuguita):
    tortuguita.right(90)
    yield 0
    for x in range(1, 4):
        tortuguita.left(90)
        tortuguita.forward(size)
        yield x
    tortuguita.left(90)
    tortuguita.forward(size)
    tortuguita.left(90)


def outter_triangle_fractal_stepper(size, new_size_deffer, tortuguita):
    step_size = (size - new_size_deffer(size)) / 2
    tortuguita.forward(step_size)
    tortuguita.right(60)
    yield 0
    for x in range(1, 3):
        tortuguita.right(-60)
        tortuguita.forward(size - step_size)
        tortuguita.left(120)
        tortuguita.forward(step_size)
        tortuguita.right(60)
        yield x
    tortuguita.right(-60)
    tortuguita.forward(size - step_size)
    tortuguita.left(120)


def outter_triangle_fractal_stepper_upper(size, new_size_deffer, tortuguita):
    eraser_factor = 1.7
    step_size = (size - new_size_deffer(size)) / 2
    tortuguita.left(60)
    tortuguita.penup()
    tortuguita.forward(step_size)
    tortuguita.pendown()
    yield 0
    now_color = tortuguita.color()
    now_pensize = tortuguita.pensize()
    tortuguita.pensize(eraser_factor * now_pensize)
    tortuguita.color('white')
    tortuguita.forward(size - 2 * step_size)
    tortuguita.pensize(now_pensize)
    tortuguita.color(now_color[0], now_color[1])
    tortuguita.penup()
    tortuguita.forward(step_size)
    tortuguita.right(120)
    tortuguita.forward(step_size)
    tortuguita.pendown()
    yield 1
    now_color = tortuguita.color()
    now_pensize = tortuguita.pensize()
    tortuguita.pensize(eraser_factor * now_pensize)
    tortuguita.color('white')
    tortuguita.forward(size - 2 * step_size)
    tortuguita.pensize(now_pensize)
    tortuguita.color(now_color[0], now_color[1])
    tortuguita.penup()
    tortuguita.forward(step_size)
    tortuguita.right(120)
    tortuguita.pendown()
    now_color = tortuguita.color()
    now_pensize = tortuguita.pensize()
    tortuguita.pensize(eraser_factor * now_pensize)
    tortuguita.color('white')
    tortuguita.forward(size)
    tortuguita.right(180)
    tortuguita.pensize(now_pensize)
    tortuguita.color(now_color[0], now_color[1])


def stopped_stepper(size, new_size_deffer, tortuguita):
	yield 0


def angled_stepper(size, new_size_deffer, tortuguita, n):
    angle = 360 / n
    inscrit_size = size_inscrit_polygon(size, n)
    tortuguita.left(180)
    yield 0
    tortuguita.left(-180)
    for x in range(1, n):
        tortuguita.penup()
        tortuguita.left(angle / 2)
        tortuguita.forward(inscrit_size)
        tortuguita.pendown()
        tortuguita.left(angle / 2 + 180)
        yield x
        tortuguita.left(-180)
    tortuguita.penup()
    tortuguita.left(angle / 2)
    tortuguita.forward(inscrit_size)
    tortuguita.pendown()
    tortuguita.left(angle / 2)


def gen_angled_stepper(n):
    return lambda size, new_size_deffer, tortuguita : angled_stepper(size, new_size_deffer, tortuguita, n)