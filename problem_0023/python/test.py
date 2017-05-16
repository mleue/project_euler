import unittest
import e0023

class Test0023(unittest.TestCase):
  def test_proper_divisors(self):
    """test proper divisors on an example"""
    test_case = ({1, 2, 4, 7, 14}, 28)
    self.assertEqual(e0023.proper_divisors(test_case[1]), test_case[0])

  def test_is_abundant(self):
    """test is abundant on an example"""
    test_cases = ((True, 12), (False, 13))
    for test_case in test_cases:
      self.assertEqual(e0023.is_abundant(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
