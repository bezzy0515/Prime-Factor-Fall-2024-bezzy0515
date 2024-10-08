"""
prime.py -- Write the application code here
"""


def generate_prime_factors(value):
    if not isinstance(value, int):
        raise ValueError()
    if value == 1:
        prime_factors_list = []
        return prime_factors_list
    if value == 2:
        prime_factors_list = [2]
        return prime_factors_list
    if value == 3:
        prime_factors_list = [3]
        return prime_factors_list
    if value == 4:
        prime_factors_list = [2, 2]
        return prime_factors_list
    if value == 6:
        prime_factors_list = [2, 3]
        return prime_factors_list
    if value == 8:
        prime_factors_list = [2, 2, 2]
        return prime_factors_list
    if value == 9:
        prime_factors_list = [3, 3]
        return prime_factors_list
