import unittest
import e0025

class Test0025(unittest.TestCase):
  def test_fib(self):
    """test fibonacci generator on the first 5 terms"""
    test_case = (12, 3)
    count = 1
    fibonacci = iter(e0025.fib())
    while len(str(next(fibonacci))) < test_case[1]:
      count += 1
    self.assertEqual(test_case[0], count)

if __name__ == '__main__':
  unittest.main()
