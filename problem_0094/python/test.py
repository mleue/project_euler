import unittest
import e0094

class Test0094(unittest.TestCase):
  def test_equal_sided_triangle_area(self):
    test_case = (12.0, (5, 6))
    self.assertEqual(e0094.equal_sided_triangle_area(*test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
