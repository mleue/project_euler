import unittest
from e0002 import fibonacci, solution

class Test0002(unittest.TestCase):

  def test_fibonacci_example(self):
    """it should get the example fibonacci sequence correct"""
    test_case = ([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89], 100)
    fibonacci_numbers = list(fibonacci(test_case[1]))
    self.assertEqual(fibonacci_numbers, test_case[0])

  def test_solution_example(self):
    test_case = (44, 100)
    self.assertEqual(solution(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
