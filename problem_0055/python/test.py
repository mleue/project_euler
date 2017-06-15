import unittest
import e0055

class Test0055(unittest.TestCase):
  def test_is_palindrome(self):
    test_cases = ((True, '7337'), (True, '121'), (False, '137'))
    for test_case in test_cases:
      self.assertEqual(e0055.is_palindrome(test_case[1]), test_case[0])

  def test_is_not_lychrel_number(self):
    test_cases = ((True, '47'), (True, '349'), (False, '196'), (False, '4994'))
    for test_case in test_cases:
      self.assertEqual(e0055.is_not_lychrel_number(test_case[1], set()), test_case[0])

if __name__ == '__main__':
  unittest.main()
