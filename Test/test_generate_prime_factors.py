import pytest
import prime

"""
Step #1
Verify data type is integer.
"""


def test_data_not_integer():
    with pytest.raises(ValueError):
        prime.generate_prime_factors("test")
    with pytest.raises(ValueError):
        prime.generate_prime_factors(4.3)