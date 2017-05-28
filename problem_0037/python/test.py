import unittest
import e0037

class Test0037(unittest.TestCase):
  def test_primes_below_thresh(self):
    """test prime generator below threshold on an example"""
    test_case = ([2, 3, 5, 7, 11, 13, 17, 19], 20)
    self.assertEqual(e0037.primes_below_thresh(test_case[1]), test_case[0])

  def test_is_left_right_truncatable_prime(self):
    """test on the given example"""
    test_cases = ((True, '3797'), (False, '3796'))
    thresh = 1000000
    prime_str_set = set([str(prime) for prime in e0037.primes_below_thresh(thresh)])
    for test_case in test_cases:
      self.assertEqual(e0037.is_left_right_truncatable(test_case[1], prime_str_set), test_case[0])

if __name__ == '__main__':
  unittest.main()
