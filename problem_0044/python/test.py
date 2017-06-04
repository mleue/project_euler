import unittest
import e0044

class Test0044(unittest.TestCase):
  def test_generate_pentagonal_numbers_below_thresh(self):
    """test on the example list"""
    test_case = ([1, 5, 12, 22, 35, 51, 70, 92], 100)
    self.assertEqual(list(e0044.generate_pentagonal_numbers_below_thresh(test_case[1])), test_case[0])

if __name__ == '__main__':
  unittest.main()
