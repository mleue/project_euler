import unittest
import e0051

class Test0051(unittest.TestCase):
  def test_prime_sieve(self):
    """test on primes below 20"""
    test_case = ([2,3,5,7,11,13,17,19], 20)
    self.assertEqual(e0051.prime_sieve(test_case[1]), test_case[0])

  def test_get_reoccuring_digit(self):
    """test on some examples"""
    test_cases = ((0, (56003, 2)), (None, (56013, 2)))
    for test_case in test_cases:
      self.assertEqual(e0051.get_reoccuring_digit(*test_case[1]), test_case[0])

  def test_create_number_variations(self):
    """test on one example"""
    test_case = ([56003, 56113, 56223, 56333, 56443, 56553, 56663, 56773, 56883, 56993], (56003, 0))
    self.assertEqual(e0051.create_number_variations(*test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
