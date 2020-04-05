import unittest
from typing import List
from code import PrimeFactors


class TestPrimeFactors(unittest.TestCase):
    def _test_prime_factors(self, input: int, expected: List[int]):
        obj = PrimeFactors(input)
        self.assertEqual(obj.result, expected)

    def test_number_one(self):
        self._test_prime_factors(1, [])

    def test_number_two(self):
        self._test_prime_factors(2, [2])

    def test_number_three(self):
        self._test_prime_factors(3, [3])

    def test_number_four(self):
        self._test_prime_factors(4, [2, 2])

    def test_number_six(self):
        self._test_prime_factors(6, [2, 3])

    def test_number_eight(self):
        self._test_prime_factors(8, [2, 2, 2])

    def test_number_nine(self):
        self._test_prime_factors(9, [3, 3])


if __name__ == "__main__":
    unittest.main()
