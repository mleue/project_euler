import unittest
import e0038

class Test0038(unittest.TestCase):
  def test_is_1_to_9_pandigital(self):
    """test 1-9 pandigitality on some examples"""
    test_cases = ((True, '192384576'), (True, '918273645'), (False, '134113456'))
    for test_case in test_cases:
      self.assertEqual(e0038.is_1_to_9_pandigital(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
