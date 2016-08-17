#!/bin/env python3

from math import cos,pi

def size_inscrit_polygon(size, n):
    return size * (2 - 2 * cos(2*pi / n))**0.5