import unittest
import e0009

class Test0009(unittest.TestCase):
  def test_pythagorean_triplet(self):
    """test pythagorean triplet on the example"""
    test_case = (60, 12)
    self.assertEqual(e0009.pythagorean_triplet(test_case[1]), test_case[0])

if __name__ == '__main__':
  unittest.main()
