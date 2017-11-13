from time import time
from math import sqrt, floor
from decimal import Decimal


def find_blue_balls(all_balls):
  """Return number of blue balls for a P(bb)= 1/2 probability."""
  all_balls_equ = 1 + 2 * all_balls * (all_balls-1)
  return Decimal(1 + sqrt(all_balls_equ))/2


if __name__ == '__main__':
  curr, upper = 10, 2000000000000
  # curr, upper = 1000000000001, 2000000000000
  prev_find, factor = None, 5.7
  while curr < upper:
    all_balls = curr
    blue_balls = find_blue_balls(all_balls)
    # if blue_balls.is_integer():
    if blue_balls % 1 == 0:
      if blue_balls*(blue_balls-1)*2 == all_balls*(all_balls-1):
        print(blue_balls)
        blue_balls = int(blue_balls)
        print("all: {},\t blue: {},\t red: {}"
              .format(all_balls, blue_balls, all_balls-blue_balls))
        if prev_find is not None:
          factor = all_balls/prev_find
          prev_find = all_balls
          print(factor)
        else:
          prev_find = all_balls
        curr = floor(all_balls*factor)
        curr -= 10
        continue
    curr += 1
