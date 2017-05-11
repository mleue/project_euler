import unittest
import e0017

class Test0017(unittest.TestCase):
  def test_number_letter_counts(self):
    """test number letter counts on an example"""
    test_case = (19, range(1, 6))
    self.assertEqual(e0017.number_letter_counts(test_case[1]), test_case[0])

  def test_number_to_words(self):
    """test number to words on some examples"""
    test_cases = (('six', 6), ('fifteen', 15), ('forty-six', 46), ('one hundred and sixty-seven', 167), ('two hundred', 200), ('one thousand', 1000))
    for test_case in test_cases:
      self.assertEqual(e0017.number_to_words(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
