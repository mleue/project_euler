import unittest
import e0010

class Test0010(unittest.TestCase):
  def test_prime_generator(self):
    """test the prime generator on a sequence of known primes"""
    test_case = ([2, 3, 5, 7, 11, 13, 17, 19], 20)
    self.assertEqual(e0010.prime_generator(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
