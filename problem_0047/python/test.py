import unittest
import e0047

class Test0047(unittest.TestCase):
  def test_prime_sieve(self):
    """test on primes below 20"""
    test_case = ([2, 3, 5, 7, 11, 13, 17, 19], 20)
    self.assertEqual(e0047.prime_sieve(test_case[1]), test_case[0])

  def test_prime_factors(self):
    """test on some given examples"""
    test_cases = (([2, 7], 14), ([3, 5], 15), ([2, 2, 7, 23], 644), ([2, 17, 19], 646))
    primes = e0047.prime_sieve(100)
    prime_set = set(primes)
    for test_case in test_cases:
      self.assertEqual(e0047.prime_factors(test_case[1], primes, prime_set), test_case[0])

  def test_combine_same(self):
    """test on the given example"""
    test_case = ({4, 7, 23}, [2, 2, 7, 23])
    self.assertEqual(e0047.combine_same(test_case[1]), test_case[0])

  def test_consecutive_distinct_prime_factors(self):
    """test on the examples"""
    test_cases = ((14, 2), (644, 3))
    for test_case in test_cases:
      self.assertEqual(e0047.consecutive_distinct_prime_factors(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
