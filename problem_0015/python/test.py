import unittest
import e0015

class Test0015(unittest.TestCase):
  def test_factorial(self):
    """test creation of factorial on some examples"""
    test_cases = [(1, 0), (1, 1), (2, 2), (6, 3), (24, 4), (3628800, 10)]
    for test_case in test_cases:
      self.assertEqual(e0015.factorial(test_case[1]), test_case[0])

  def test_lattice_path_permutations(self):
    """test creation of factorial on some examples"""
    test_cases = [(6, 2), (20, 3)]
    for test_case in test_cases:
      self.assertEqual(e0015.lattice_path_permutations(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
