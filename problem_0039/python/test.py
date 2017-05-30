import unittest
import e0039

class Test0039(unittest.TestCase):
  def test_number_of_possible_right_triangles(self):
    test_case = (3, 120)
    self.assertEqual(e0039.number_of_possible_right_triangles(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
