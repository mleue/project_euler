import time
import math

def equal_sided_triangle_area(a, c):
  """return area of equal sided (a==b) triangle with sides a1, a2, c"""
  return (c/2) * math.sqrt(a**2 - c**2/4)

if __name__ == '__main__':
  a = 3
  perimeters_sum = 0
  thresh = 333333333

  while a < thresh:
    c = a - 1
    if equal_sided_triangle_area(a, c).is_integer():
      print(a + a + c)
      perimeters_sum += (a + a + c)
      a = 12*a - a
      continue
    c = a + 1
    if equal_sided_triangle_area(a, c).is_integer():
      print(a + a + c)
      perimeters_sum += (a + a + c)
      a = 12*a - a
      continue
    a += 2

  print(perimeters_sum)
