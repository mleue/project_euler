import unittest
from e0005 import numbers_to_check, smallest_number_divisible_by_range

class Test0005(unittest.TestCase):
  def test_numbers_to_check_correct_example(self):
    """should get the examples right"""
    test_cases = (([6,7,8,9,10][::-1], range(1, 11)), ([11,12,13,14,15,16,17,18,19,20][::-1], range(1, 21)))
    for test_case in test_cases:
      self.assertEqual(numbers_to_check(test_case[1]), test_case[0])

  def test_smallest_number_divisible_by_range_correct_example(self):
    """should get the example right"""
    test_case = (2520, range(1, 11))
    self.assertEqual(smallest_number_divisible_by_range(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
