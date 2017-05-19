import unittest
import e0028

class Test0028(unittest.TestCase):
  def test_spiral_corner_generator(self):
    """test spiral corner generator on an example"""
    test_case = (101, 5)
    self.assertEqual(sum(e0028.spiral_corner_generator(test_case[1])), test_case[0])

if __name__ == '__main__':
  unittest.main()
