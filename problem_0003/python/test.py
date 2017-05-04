import unittest
from e0003 import largest_prime_factor, prime_numbers

class Test0003(unittest.TestCase):
  def test_prime_numbers(self):
    """it should generate the known sequence of primes below 30"""
    test_case = ([2,3,5,7,11,13,17,19,23,29], 30)
    self.assertEqual(list(prime_numbers(test_case[1])), test_case[0])

  def test_largest_prime_factor(self):
    """it should get the example right"""
    test_case = (29, 13195)
    self.assertEqual(largest_prime_factor(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
