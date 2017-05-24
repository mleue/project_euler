import unittest
import e0033

class Test0033(unittest.TestCase):
  def test_is_curious_fraction(self):
    """test on the given example"""
    test_cases = ((True, ('49', '98')), (False, ('11', '12')))
    for test_case in test_cases:
      self.assertEqual(e0033.is_curious_fraction(*test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
