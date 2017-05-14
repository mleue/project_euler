import unittest
import e0021

class Test0021(unittest.TestCase):
  def test_proper_divisors(self):
    """test proper divisors on an example"""
    test_case = ({1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}, 220)
    self.assertEqual(e0021.proper_divisors(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
