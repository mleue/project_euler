import unittest
import e0045

class Test0045(unittest.TestCase):
  def test_is_int(self):
    """test on some examples"""
    test_cases = ((True, 3.0), (False, 3.1), (False, 2.9))
    for test_case in test_cases:
      self.assertEqual(e0045.is_int(test_case[1]), test_case[0])

  def test_quadratic_solution(self):
    """test on an example"""
    test_case = (165.0, (3, -1, -2*40755))
    self.assertEqual(e0045.quadratic_solution(*test_case[1]), test_case[0])

  def test_is_triangle_number(self):
    """test on the given example"""
    test_cases = ((True, 40755), (False, 9))
    for test_case in test_cases:
      self.assertEqual(e0045.is_triangle_number(test_case[1]), test_case[0])

  def test_is_pentagonal_number(self):
    """test on the given example"""
    test_cases = ((True, 40755), (False, 9))
    for test_case in test_cases:
      self.assertEqual(e0045.is_pentagonal_number(test_case[1]), test_case[0])

  def test_generate_hexagonals(self):
    """test on the first 5"""
    test_case = ([1, 6, 15, 28, 45], 1)
    hexagonals = []
    hex_generator = e0045.generate_hexagonals(test_case[1])
    for _ in range(5):
      hexagonals.append(next(hex_generator))
    self.assertEqual(test_case[0], hexagonals)

if __name__ == '__main__':
  unittest.main()
