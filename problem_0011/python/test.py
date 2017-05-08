import unittest
import e0011

class Test0011(unittest.TestCase):
  def test_import_grid_from_file(self):
    """test if we can succesfully import the grid file line by line"""
    test_case = ([1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48], 'grid.txt')
    self.assertEqual(e0011.import_grid_from_file(test_case[1])[-1], test_case[0])

  def test_create_grid_matrix(self):
    """test create grid matrix on example"""
    test_cases = ((8, (0, 0)), (48, (19, 19)))
    grid = e0011.import_grid_from_file('grid.txt')
    for test_case in test_cases:
      self.assertEqual(e0011.create_grid_matrix(grid)[test_case[1]], test_case[0])

  def test_build_list_adjacent_n_correct_elements(self):
    """test build list adjacent n on the example matrix"""
    test_case = ([[(0,0), (1,0), (2,0), (3,0)], [(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,1), (2,2), (3,3)]], 4)
    matrix = e0011.create_grid_matrix(e0011.import_grid_from_file('grid.txt'))
    self.assertEqual(e0011.build_list_adjacent_n(matrix, test_case[1])[:3], test_case[0])

  def test_build_list_adjacent_n_correct_length(self):
    """test build list adjacent n on the example matrix"""
    test_case = (4*20*20, 4)
    matrix = e0011.create_grid_matrix(e0011.import_grid_from_file('grid.txt'))
    self.assertEqual(len(e0011.build_list_adjacent_n(matrix, test_case[1])), test_case[0])

if __name__ == '__main__':
  unittest.main()
