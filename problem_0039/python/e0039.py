import math
from collections import defaultdict

#conditions:
# 1) a^2 + b^2 = c^2
# 2) a + b + c = p
# 3) a < b < c == c > (1/3)*p
# 4) type(a, b, c) == int

def is_int(number_float):
  """return whether the float can be expressed as an int"""
  return number_float == int(number_float)

if __name__ == '__main__':
  perimeters = defaultdict(int)
  for c in range(333, 500):
    for a in range(1, c):
      #TODO: or use quadratic formula for this?
      b = math.sqrt(c**2 - a**2)
      if is_int(b):
        perimeters[a+b+c] += 1

  print(max(perimeters, key=lambda k: perimeters[k]))
