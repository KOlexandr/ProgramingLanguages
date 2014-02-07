from math import sqrt

__author__ = 'Olexandr'

"""
Task: 1
"""


#find discriminant for square equation
d = lambda a, b, c: b * b - 4 * a * c


#solve quadratic equation with inner if
solve_square_equation_if = lambda a, b, c: [(-b + sqrt(d(a, b, c))) / (2 * a), (-b - sqrt(d(a, b, c))) / (2 * a)] if d(a, b, c) > 0 else None if d(a, b, c) < 0 else -b/(2*a)


#solve quadratic equation without if
solve_square_equation = lambda a, b, c: (d(a, b, c) < 0 and "complex roots") or (d(a, b, c) == 0 and -b/(2*a)) or [(-b + sqrt(d(a, b, c))) / (2 * a), (-b - sqrt(d(a, b, c)))/(2*a)]

""" tests """
print("with if:", solve_square_equation_if(-1, 0, 1))
print("without if:", solve_square_equation(-1, 0, 1), "\n")

print("with if:", solve_square_equation_if(1, 0, 1))
print("without if:", solve_square_equation(1, 0, 1), "\n")

print("with if:", solve_square_equation_if(2, 4, 2))
print("without if:", solve_square_equation(2, 4, 2))