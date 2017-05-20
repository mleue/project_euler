import unittest
import e0029

class Test0029(unittest.TestCase):
  def test_distinct_combinations(self):
    """test on the given example"""
    test_case = (15, 5)
    self.assertEqual(e0029.distinct_combinations(test_case[1], test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
