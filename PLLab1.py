from functools import reduce
from math import sqrt

__author__ = 'Olexandr'

#solve quadratic equation
solve_square_equation = lambda a, b, c: [(-b + sqrt(b * b - 4 * a * c)) / (2 * a),
                                         (-b - sqrt(b * b - 4 * a * c)) / (
                                             2 * a)] if b * b - 4 * a * c > 0 else \
    None if b * b - 4 * a * c < 0 else -b / (2 * a)
print(solve_square_equation(-1, 0, 1))


#verify is number is palindrome
is_palindrome = lambda n: str(n) == reduce(lambda x, y: y + x, str(n))
print(is_palindrome(121))

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


#verify is number perfect
is_perfect_number = lambda n: n == reduce(lambda x, y: x + y, filter(lambda d: n % d == 0, range(1, int(n / 2) + 1)), 0)
print(is_perfect_number(28))


#verify is number simple
is_simple_number = lambda n: 0 == reduce(lambda x, y: x + y, filter(lambda d: n % d == 0, range(2, int(sqrt(n)) + 1)),
                                         0)
print(is_simple_number(997))


#find nth simple number
#for n > 0
find_next_simple = lambda n: n if is_simple_number(n) else find_next_simple(n + 1)
find_nth_simple = lambda n: reduce(lambda x, y: find_next_simple(x + 1), range(n), 1)
print(find_nth_simple(1))


#find nth perfect number
#for n > 0
find_next_perfect = lambda n: n if is_perfect_number(n) else find_next_perfect(n + 1)
find_nth_perfect = lambda n: reduce(lambda x, y: find_next_perfect(x + 1), range(n), 1)
print(find_nth_perfect(2))

find_nth_needle = lambda next_needle: lambda n: reduce(lambda x, y: next_needle(x + 1), range(n), 1)
#find nth simple number
print(find_nth_needle(find_next_simple)(1))
#find nth perfect number
print(find_nth_needle(find_next_perfect)(1))


#find multiplication of n first simple numbers
multiply_of_n_simple = lambda n: reduce(lambda x, y: x * y, [find_nth_simple(x) for x in range(1, n + 1)])
print(multiply_of_n_simple(5))


#find greatest common divisor
gcd = lambda a, b: a if b == 0 else gcd(b, a % b)
print(gcd(840, 396))


#find least common multiple
lcm = lambda a, b: a / gcd(a, b) * b
print(lcm(840, 396))


#find greatest common divisor least common multiple together
gcd_lcm = lambda a, b: [("gcd", gcd(a, b)), ("lcm", lcm(a, b))]
print(gcd_lcm(840, 396))


#find sqrt
iterate = lambda f, g, stop_val: f(g) if (lambda x, y: abs((x - y) / x) / x < stop_val)(g, f(g)) else iterate(f, f(g),
                                                                                                              stop_val)
my_sqrt = lambda x, stop_val: iterate(lambda y: (y + x / y) / 2, 1, stop_val)
print(my_sqrt(9, 0.00001))
print(sqrt(9))