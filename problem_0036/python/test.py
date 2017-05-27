import unittest
import e0036

class Test0036(unittest.TestCase):
  def test_dec_to_base2(self):
    """test conversion on an example"""
    test_cases = (('1001001001', 585), ('001', 4))
    for test_case in test_cases:
      self.assertEqual(e0036.dec_to_base2(test_case[1]), test_case[0])

  def test_is_palindromic(self):
    """test on some examples"""
    test_cases = ((True, '585'), (True, '1001001001'), (False, '586'))
    for test_case in test_cases:
      self.assertEqual(e0036.is_palindromic(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
