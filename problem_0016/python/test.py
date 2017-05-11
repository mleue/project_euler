import unittest
import e0016

class Test0016(unittest.TestCase):
  def test_digit_sum(self):
    """test digit sum on an example"""
    test_case = (26, 32768)
    self.assertEqual(e0016.digit_sum(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
