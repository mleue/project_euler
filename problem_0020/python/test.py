import unittest
import e0020

class Test0020(unittest.TestCase):
  def test_factorial(self):
    """test factorial generator on an example"""
    test_case = (3628800, 10)
    self.assertEqual(e0020.factorial(test_case[1]), test_case[0])

  def test_sum_of_digits(self):
    """test sum of digits on an example"""
    test_case = (27, 3628800)
    self.assertEqual(e0020.sum_of_digits(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
