#!/bin/env python3

import turtle
from fractalis.unit import *
from fractalis.stepper import *
from fractalis.meta import *


def example_triforce(wn, tortuguita):
    draw_fractal(120, 3, tortuguita, draw_triangle, lambda x: x / 2, triangle_fractal_stepper)


def example_outter_triangle(wn, tortuguita):
    draw_fractal(120, 3, tortuguita, draw_triangle, lambda x: x / 3, outter_triangle_fractal_stepper)


def example_triangle_stepper_cleaner(wn, tortuguita):
    draw_fractal(120, 3, tortuguita, draw_triangle, lambda x: 2 * x / 3, outter_triangle_fractal_stepper_upper)


def example_dummy_circle(wn, tortuguita):
    draw_fractal(120, 5, tortuguita, draw_circle, lambda x: 0.7 * x, stopped_stepper)


def example_interesting_circle_triangle(wn, tortuguita):
    draw_fractal(80, 4, tortuguita, draw_circle, lambda x: x/2, gen_angled_stepper(3))


def example_interesting_circle_square(wn, tortuguita):
    draw_fractal(80, 4, tortuguita, draw_circle, lambda x: x/2, gen_angled_stepper(4))


def example_interesting_circle_hexagon(wn, tortuguita):
    draw_fractal(80, 3, tortuguita, draw_circle, lambda x: x/3, gen_angled_stepper(6))


def example_cutter_3_lvl(wn, tortuguita):
    draw_fractal(120, 3, tortuguita, draw_cutter, lambda x: 2 * x / 3, outter_triangle_fractal_stepper_upper)


def example_cutter_5_lvl(wn, tortuguita):
    draw_fractal(120, 5, tortuguita, draw_cutter, lambda x: x / 2, outter_triangle_fractal_stepper_upper)


def example_mid_square(wn, tortuguita):
    draw_fractal(120, 3, tortuguita, draw_square, lambda x: x / 3, square_fractal_mid_stepper)


def example_corner_square(wn, tortuguita):
    draw_fractal(120, 4, tortuguita, draw_square, lambda x: 2*x / 5, square_fractal_corner_stepper)


def renew(wn):
    wn.reset()
    try:
        return wn.turtles()[0]
    except IndexError:
        return turtle.Turtle()


class example_runner:
    def __init__(self, clicklist):
        self.i = 0
        self.clicklist = clicklist

    def example_clicker(self, wn):
        index = self.i
        tortuguita = renew(wn)
        example = self.get_example(wn, index)
        self.i += 1
        print('testando exemplo %d: %s' % (index, example))
        example(wn, tortuguita)
        print('terminou a impressão (%s)' % example)

    def get_example(self, wn, index):
        try:
            return self.clicklist[index]
        except IndexError:
            return lambda window, tortuguita: wn.bye()


def runall():
    clicklist = [example_triforce, example_outter_triangle, example_triangle_stepper_cleaner, example_dummy_circle,
                 example_interesting_circle_triangle, example_interesting_circle_hexagon,
                 example_interesting_circle_square, example_cutter_3_lvl, example_cutter_5_lvl, example_mid_square,
                 example_corner_square]
    example = example_runner(clicklist)
    wn = turtle.Screen()
    wn.title('Continue a clicar')
    wn.textinput('Olá', 'Os exemplos são dados a cada clique.\nPortanto, continue a clicar!')
    wn.onscreenclick(lambda x, y: example.example_clicker(wn))
    wn.mainloop()
    print('saiu do mainloop!')
