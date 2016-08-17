#!/bin/env python3

def gen_draw_polygon(n):
    return lambda size,tortuguita: draw_polygon(n, size, tortuguita)


def draw_polygon(n, size, tortuguita):
    for x in range(0, n):
        tortuguita.forward(size)
        tortuguita.left(360/n)


draw_triangle = gen_draw_polygon(3)


draw_square = gen_draw_polygon(4)


def draw_cutter(size, tortuguita):
	tortuguita.left(60)
	tortuguita.forward(size)
	tortuguita.right(120)
	tortuguita.forward(size)
	tortuguita.right(120)
	tortuguita.penup()
	tortuguita.forward(size)
	tortuguita.left(180)
	tortuguita.pendown()

def draw_circle(size, tortuguita):
    tortuguita.circle(size)