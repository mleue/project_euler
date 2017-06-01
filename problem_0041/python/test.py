import unittest
import e0041

class Test0041(unittest.TestCase):
  def test_is_n_pandigital(self):
    """test on some examples"""
    test_cases = ((True, '2143'), (True, '53241'), (False, '552341'))
    for test_case in test_cases:
      self.assertEqual(e0041.is_n_pandigital(test_case[1]), test_case[0])

  def test_prime_sieve(self):
    """test on the first 20"""
    test_case = ([2, 3, 5, 7, 11, 13, 17, 19], 20)
    self.assertEqual(e0041.prime_sieve(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
