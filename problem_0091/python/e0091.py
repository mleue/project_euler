from collections import Counter
from factorize import get_prime_factors


# TODO we really only need a gcd function in here
prime_factors = get_prime_factors(100)
prime_factors[1] = [1]


def product_over_sequence(seq):
  """Return product over sequence."""
  product = 1
  for el in seq:
    product *= el
  return product


def reduce(n1, n2):
  """Return reduced form of n1/n2 if possible."""
  prime_factors_1 = prime_factors[n1]
  prime_factors_2 = prime_factors[n2]
  common_prime_factors = list((Counter(prime_factors_1) & Counter(prime_factors_2)).elements())
  gcd = product_over_sequence(common_prime_factors)
  return n1//gcd, n2//gcd


def number_right_triangles(coord_thresh):
  """Return number of right triangles in OPQ for P, Q coords <= coord thresh."""
  count = 0
  # right angle at P cases
  for x1 in range(coord_thresh+1):
    for y1 in range(coord_thresh+1):
      if x1 > 0 and y1 > 0:
        # OP slope is y1/x1
        # to form a right triangle we need to find the perpendicular line PQ
        # this is -x1/y1
        # any integer x2,y2 on that line is then a solution for Q
        x2, y2 = x1, y1
        step_x, step_y = reduce(x1, y1)
        while True:
          x2 += step_y
          y2 -= step_x
          if x2 <= coord_thresh and y2 >= 0:
            count += 1
          else:
            break
  print(count)
  # double this amount for all right angle at Q cases
  count *= 2

  print(count)
  # add all cases where the right angle is at O (i.e. x1==0, y2==0)
  count += 3*coord_thresh*coord_thresh
  print(count)
  return count


if __name__ == '__main__':
  assert reduce(16, 4) == (4, 1)
  assert reduce(6, 4) == (3, 2)
  assert reduce(49, 7) == (7, 1)
  assert reduce(49, 49) == (1, 1)
  # assert number_right_triangles(2) == 14
  print(number_right_triangles(50))
