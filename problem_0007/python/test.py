import unittest
from e0007 import prime_generator, nth_prime 

class Test0007(unittest.TestCase):
  def test_prime_generator(self):
    """it should generate the known sequence of primes below 30"""
    test_case = ([2,3,5,7,11,13,17,19,23,29], 30)
    self.assertEqual(list(prime_generator(test_case[1])), test_case[0])

  def test_nth_prime(self):
    """it should get the example right"""
    test_case = (13, 6)
    self.assertEqual(nth_prime(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
