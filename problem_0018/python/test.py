import unittest
import e0018

class Test0018(unittest.TestCase):
  def test_read_triangle(self):
    """test reading the triangle file by comparing some numbers of the last row"""
    test_case = ([60, 4, 23], 'numberTriangle.txt')
    self.assertEqual(e0018.read_triangle(test_case[1])[-1][-3:], test_case[0])

  def test_add_lists_elementwise(self):
    """test adding lists elementwise on an example"""
    test_case = ([3, 4, 5], [[1,1,1], [2,3,4]])
    self.assertEqual(e0018.add_lists_elementwise(*test_case[1]), test_case[0])

  def test_reduce_list_consecutive_max_neighbors(self):
    """test reducing list to consecutive max neighbors on an example"""
    test_case = ([5,8,8], [4,5,8,3])
    self.assertEqual(e0018.reduce_list_consecutive_max_neighbors(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
