import unittest
import e0022

class Test0022(unittest.TestCase):
  def test_char_score(self):
    """test char score on some examples"""
    test_cases = ((3, 'C'), (1, 'A'), (26, 'Z'))
    for test_case in test_cases:
      self.assertEqual(e0022.char_score(test_case[1]), test_case[0])

  def test_read_names_file(self):
    """test reading the names file"""
    test_case = ('ALONSO', 'names.txt')
    self.assertIn(test_case[0], e0022.read_names_file(test_case[1]))

if __name__ == '__main__':
  unittest.main()
