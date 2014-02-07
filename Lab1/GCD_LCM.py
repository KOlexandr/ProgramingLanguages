__author__ = 'Olexandr'

"""
Task: 9
"""


#find greatest common divisor with if
gcd_if = lambda a, b: a if b == 0 else gcd_if(b, a % b)
print(gcd_if(840, 396))


#find greatest common divisor without if
gcd = lambda a, b: (b == 0 and a) or gcd(b, a % b)
print(gcd(840, 396))


#find least common multiple
lcm = lambda a, b: a / gcd(a, b) * b
print(lcm(840, 396))


#find greatest common divisor least common multiple together
gcd_lcm = lambda a, b: [("gcd", gcd(a, b)), ("lcm", lcm(a, b))]
print(gcd_lcm(840, 396))