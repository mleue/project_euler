import unittest
import e0013

class Test0013(unittest.TestCase):
  def test_transpose_2d_list(self):
    """test on an example"""
    test_case = ([(1,4,7), (2,5,8), (3,6,9)], [[1,2,3], [4,5,6], [7,8,9]])
    self.assertEqual(e0013.transpose_2d_list(test_case[1]), test_case[0])

  def test_read_numbers_file(self):
    """test reading the numbers file by checking against the last 5 digits of the last number"""
    test_case = ([3,1,6,9,0], 'numbers.txt')
    self.assertEqual(e0013.read_numbers_file(test_case[1])[-1][-5:], test_case[0])

  def test_written_sum(self):
    """test the written-style summation on an example"""
    test_case = ([int(digit) for digit in str(123+456+789)] , [[1,2,3], [4,5,6], [7,8,9]])
    self.assertEqual(e0013.written_sum(test_case[1]), test_case[0])

  def test_carry_over_reduce(self):
    """test the carry over reduce on an example"""
    test_case = ([1, 3, 6, 8] , [12, 15, 18])
    self.assertEqual(e0013.carry_over_reduce(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
