#!/bin/env python3

def draw_fractal(size, level, tortuguita, simple_draw, new_size_deffer, fractal_stepper):
	simple_draw(size, tortuguita)
	if (level > 0):
		old_speed = tortuguita.speed()
		tortuguita.speed(4*tortuguita.speed())
		new_size = new_size_deffer(size)
		new_level = level - 1
		for steps in fractal_stepper(size, new_size_deffer, tortuguita):
			draw_fractal(new_size, new_level, tortuguita, simple_draw, new_size_deffer, fractal_stepper)
		tortuguita.speed(old_speed)
