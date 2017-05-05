import unittest
from e0004 import is_palindromic, create_palindromic_numbers, largest_palindromic_number_as_product, is_product_of_two_n_digit_numbers, get_number_of_digits

class Test0004(unittest.TestCase):
  def test_is_palindromic_correct_examples(self):
    """it should get some correct example palindromes right"""
    test_cases = ((True, 9009), (True, 13531), (True, 1), (True, 191), (True, 99999999))
    for test_case in test_cases:
      self.assertEqual(is_palindromic(test_case[1]), test_case[0])

  def test_is_palindromic_bad_examples(self):
    """it should get some bad example palindromes right"""
    test_cases = ((False, 90), (False, 13541), (False, 12), (False, 193), (False, 99989999))
    for test_case in test_cases:
      self.assertEqual(is_palindromic(test_case[1]), test_case[0])

  def test_is_palindromic_bad_input_negative(self):
    """it should fail on inputting a negative number"""
    test_case = -5
    self.assertRaises(ValueError, is_palindromic, test_case)

  def test_is_palindromic_bad_input_non_integer(self):
    """it should fail on inputting a non integer"""
    test_cases = ('abc', 3.7, [1, 2], (1, 3))
    for test_case in test_cases:
      self.assertRaises(TypeError, is_palindromic, test_case)

  def test_create_palindromic_numbers_correct_example(self):
    """it should get the example of all palindromes of at max 100 right"""
    test_case = ([99, 88, 77, 66, 55, 44, 33, 22, 11, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 100)
    self.assertEqual(list(create_palindromic_numbers(test_case[1])), test_case[0])

  def test_get_number_of_digits(self):
    """it should get a couple of examples right"""
    test_cases = ((2, 91), (3, 197), (1, 7), (4, 1987))
    for test_case in test_cases:
      self.assertEqual(get_number_of_digits(test_case[1]), test_case[0])

  def test_is_product_of_two_n_digit_numbers_correct_example(self):
    """it should get the example right"""
    test_case = (True, (9009, 2))
    self.assertEqual(is_product_of_two_n_digit_numbers(test_case[1][0], test_case[1][1]), test_case[0])

  def test_largest_palindromic_number_as_product_correct_example(self):
    """it should get the example right"""
    test_case = (9009, 2)
    self.assertEqual(largest_palindromic_number_as_product(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
