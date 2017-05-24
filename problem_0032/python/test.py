import unittest
import e0032

class Test0032(unittest.TestCase):
  def test_is_pandigital(self):
    """test on some of the given examples"""
    test_cases = ((True, 15234), (True, 391867254), (False, 45228))
    for test_case in test_cases:
      self.assertEqual(e0032.is_pandigital(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
