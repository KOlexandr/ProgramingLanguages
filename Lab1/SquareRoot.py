from math import sqrt

__author__ = 'Olexandr'

"""
Task: 10
"""

#iterate with inner if
iterate_if = lambda f, g, stop: f(g) if(lambda x, y: abs((x - y) / x) / x < stop)(g, f(g))else iterate_if(f, f(g), stop)

#iterate without if
iterate = lambda f, g, stop: (lambda x, y: abs((x - y) / x) / x < stop)(g, f(g)) and f(g) or iterate(f, f(g), stop)

#find sqrt
my_sqrt_if = lambda x, stop_val: iterate_if(lambda y: (y + x / y) / 2, 1, stop_val)
my_sqrt = lambda x, stop_val: iterate(lambda y: (y + x / y) / 2, 1, stop_val)

print("my sqrt with if =", my_sqrt_if(2, 0.00001))
print("my sqrt =", my_sqrt(2, 0.00001))
print("system sqrt =", sqrt(2))