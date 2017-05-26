import unittest
import e0035

class Test0035(unittest.TestCase):
  def test_primes_below_thresh(self):
    """test prime generator below threshold on an example"""
    test_case = ([2, 3, 5, 7, 11, 13, 17, 19], 20)
    self.assertEqual(e0035.primes_below_thresh(test_case[1]), test_case[0])

  def test_get_rotations(self):
    """test getting the rotations of a number str on an example"""
    test_case = (['197', '971', '719'], '197')
    self.assertEqual(list(e0035.get_rotations(test_case[1])), test_case[0])

  def test_number_of_circular_primes(self):
    """test on an example"""
    test_case = (13, 100)
    primes_list = e0035.primes_below_thresh(test_case[1])
    self.assertEqual(e0035.number_of_circular_primes(primes_list), test_case[0])

if __name__ == '__main__':
  unittest.main()
