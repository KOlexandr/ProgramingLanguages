from functools import reduce
from math import sqrt

__author__ = 'Olexandr'

"""
Tasks: 2, 3, 7, 8
"""


#verify is number perfect
is_perfect_number = lambda n: n == reduce(lambda x, y: x + y, filter(lambda d: n % d == 0, range(1, int(n / 2) + 1)), 0)
print("is perfect 28:", is_perfect_number(28))


#find nth perfect number for n > 0 with inner if
find_next_perfect_if = lambda n: n if is_perfect_number(n) else find_next_perfect_if(n + 1)
find_nth_perfect_if = lambda n: reduce(lambda x, y: find_next_perfect_if(x + 1), range(n), 1)
print("find 2nd perfect with if:", find_nth_perfect_if(2))


#find nth perfect number for n > 0 without if
find_next_perfect = lambda n: (is_perfect_number(n) and n) or find_next_perfect(n + 1)
find_nth_perfect = lambda n: reduce(lambda x, y: find_next_perfect(x + 1), range(n), 1)
print("find 2nd perfect:", find_nth_perfect_if(2))


#verify is number simple
is_simple_number = lambda n: 0 == reduce(lambda x, y: x + y, filter(lambda d: n % d == 0, range(2, int(sqrt(n))+1)), 0)
print("is simple 997:", is_simple_number(997))


#find nth simple number for n > 0 with inner if
find_next_simple_if = lambda n: n if is_simple_number(n) else find_next_simple_if(n + 1)
find_nth_simple_if = lambda n: reduce(lambda x, y: find_next_simple_if(x + 1), range(n), 1)
print("find 5th simple with if:", find_nth_simple_if(5))


#find nth simple number for n > 0 without if
find_next_simple = lambda n: (is_simple_number(n) and n) or find_next_simple(n + 1)
find_nth_simple = lambda n: reduce(lambda x, y: find_next_simple(x + 1), range(n), 1)
print("find 5th simple:", find_nth_simple(5))


find_nth_needle = lambda next_needle: lambda n: reduce(lambda x, y: next_needle(x + 1), range(n), 1)
#find nth simple number
print("find 3rd simple:", find_nth_needle(find_next_simple)(3))
#find nth perfect number
print("find 3rd perfect:", find_nth_needle(find_next_perfect)(3))


#find multiplication of n first simple numbers
multiply_of_n_simple = lambda n: reduce(lambda x, y: x * y, map(find_nth_simple, range(1, n + 1)))
print("multiplication of 5 first simple:", multiply_of_n_simple(5))