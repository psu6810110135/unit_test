
from _6810110135_.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        numbers = [1, 2, 3]
        is_prime = is_prime_list(numbers)
        self.assertTrue(is_prime)
    def test_give_4_5_6_is_not_prime(self):
        numbers = [4, 5, 6]
        is_prime = is_prime_list(numbers)
        self.assertFalse(is_prime)
    def test_give_7_8_9_is_not_prime(self):
        numbers = [7, 8, 9]
        is_prime = is_prime_list(numbers)
        self.assertFalse(is_prime)
    def test_give_11_12_13_14_15_is_not_prime(self):
        numbers = [11, 12, 13, 14, 15]
        is_prime = is_prime_list(numbers)
        self.assertFalse(is_prime)
    def test_give_0_1_is_not_prime(self):
        numbers = [0, 1]
        is_prime = is_prime_list(numbers)
        self.assertFalse(is_prime)