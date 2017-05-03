import unittest
from e0001 import multiples_of_x_below_y, solution

class Test0001(unittest.TestCase):
  def test_multiples_of_x_below_y_examples(self):
    """it should get the example correct"""
    test_cases = [([3, 6, 9], (3, 10)),
                  ([5], (5, 10))]
    for test_case in test_cases:
      multiples = multiples_of_x_below_y(test_case[1][0], test_case[1][1])
      self.assertEqual(multiples, test_case[0])

  def test_solution_example(self):
    """it should get the example correct"""
    test_case = (23, [3, 5], 10)
    sum_solution = solution(test_case[1], test_case[2])
    self.assertEqual(sum_solution, test_case[0])

if __name__ == '__main__':
  unittest.main()
