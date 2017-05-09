import unittest
import itertools
import e0012

class Test0012(unittest.TestCase):
  def test_triangle_number_generator(self):
    """test triangle number generator on first 10 known"""
    test_case = ([1, 3, 6, 10, 15, 21, 28, 36, 45, 55], 10)
    self.assertEqual(list(itertools.islice(e0012.triangle_number_generator(), test_case[1])), test_case[0])

  def test_number_of_divisors(self):
    """test the number of divisors for a known example"""
    test_case = (6, 28)
    self.assertEqual(e0012.number_of_divisors(test_case[1]), test_case[0])

  def test_triangle_number_more_than_n_divisors(self):
    """test the number of triangle divisors on the given example"""
    test_case = (28, 5)
    self.assertEqual(e0012.triangle_number_more_than_n_divisors(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
