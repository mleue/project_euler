import unittest
from e0006 import sum_square_diff_1, sum_square_diff_2

class Test0006(unittest.TestCase):
  def test_sum_square_diff_1_example(self):
    """it must get the example right"""
    test_case = (2640, range(1, 11))
    self.assertEqual(sum_square_diff_1(test_case[1]), test_case[0])

  def test_sum_square_diff_2_example(self):
    """it must get the example right"""
    test_case = (2640, range(1, 11))
    self.assertEqual(sum_square_diff_2(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
