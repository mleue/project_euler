import unittest
import e0042

class Test0042(unittest.TestCase):
  def test_letter_value(self):
    """test letter value on some examples"""
    test_cases = ((19, 'S'), (11, 'K'), (25, 'Y'), (1, 'A'))
    for test_case in test_cases:
      self.assertEqual(e0042.letter_value(test_case[1]), test_case[0])

  def test_word_value(self):
    """test word value on an example"""
    test_case = (55, 'SKY')
    self.assertEqual(e0042.word_value(test_case[1]), test_case[0])

  def test_read_words_file(self):
    """test if we correctly read the words file by checking that the last word is read"""
    test_case = ('YOUTH', 'words.txt')
    self.assertIn(test_case[0], e0042.read_words_file(test_case[1]))

  def test_triangle_numbers_below_thresh(self):
    """test on a test set"""
    test_case = ({1, 3, 6, 10, 15}, 20)
    self.assertEqual(e0042.triangle_numbers_below_thresh(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
