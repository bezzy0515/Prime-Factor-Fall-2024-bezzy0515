"""
prime.py -- Write the application code here
"""


def generate_prime_factors(value):
    if not isinstance(value, int):
        raise ValueError()
    if value == 1:
        prime_factors_list = []
        return prime_factors_list