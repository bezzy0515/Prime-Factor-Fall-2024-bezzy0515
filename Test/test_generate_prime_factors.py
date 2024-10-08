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


"""
Step #2
Return empty list when 1 is passed.
"""


def test_empty_list_ret_with_1_passed():
    null_test_list = []
    assert null_test_list == prime.generate_prime_factors(1)



