from functools import reduce

__author__ = 'Olexandr'

"""
Tasks: 4, 5
"""


#change register of letters to upper
to_upper_case = lambda m: reduce(lambda x, y: x + y, map(lambda c: c.upper(), m))
print(to_upper_case("qwERTy"))


#change register of letters to lower
to_lower_case = lambda m: reduce(lambda x, y: x + y, map(lambda c: c.lower(), m))
print(to_lower_case("qwERTy"))


#change register of letters to inverse
# inverse_case = lambda m: reduce(lambda x, y: x + y, map(lambda c: c.upper() if c != c.upper() else c.lower(), m))
inverse_case = lambda m: reduce(lambda x, y: x + y, map(lambda c: c.swapcase(), m))
print(inverse_case("qwERTy"))