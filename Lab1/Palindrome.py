from functools import reduce

__author__ = 'Olexandr'

"""
Task: 6
"""

#verify is number is palindrome
is_palindrome = lambda n: str(n) == reduce(lambda x, y: y + x, str(n))
print(is_palindrome(121))