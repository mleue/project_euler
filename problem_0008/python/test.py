import unittest
import e0008

class Test0008(unittest.TestCase):
  def test_import_number_string(self):
    """tests the import of the relevant string from file"""
    test_case1 = ('63450', 'number.txt')
    test_case2 = (1000, 'number.txt')
    self.assertEqual(e0008.import_number_string(test_case1[1])[-5:], test_case1[0])
    self.assertEqual(len(e0008.import_number_string(test_case2[1])), test_case2[0])

  def test_all_n_char_substrings(self):
    """tests all n char substrings on an example"""
    test_case = (['ab', 'bc', 'cd', 'de'], ('abcde', 2))
    self.assertEqual(list(e0008.all_n_char_substrings(*test_case[1])), test_case[0])

  def test_greatest_adjacent_product(self):
    """tests greatest adjacent product on the example"""
    test_case = (5832, (e0008.import_number_string('number.txt'), 4))
    self.assertEqual(e0008.greatest_adjacent_product(*test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
