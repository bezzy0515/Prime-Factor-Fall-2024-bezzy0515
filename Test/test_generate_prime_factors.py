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


"""
Step #3
Return list [2] when 2 is passed
"""


def test_generate_prime_factors_list_2_when_2_passed():
    two_test_list = [2]
    assert two_test_list == prime.generate_prime_factors(2)


"""
Step #4
Return list [3] when 3 is passed
"""


def test_generate_prime_factors_list_3_when_3_passed():
    three_test_list = [3]
    assert three_test_list == prime.generate_prime_factors(3)
