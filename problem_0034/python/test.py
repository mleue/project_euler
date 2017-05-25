import unittest
import e0034

class Test0034(unittest.TestCase):
  def test_factorial(self):
    """test factorial on an example"""
    test_case = (362880, 9)
    self.assertEqual(e0034.factorial(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
