import math
from decimal import Decimal, getcontext


def digit_sum(digit_str):
  """Return sum of digits."""
  return sum(int(digit) for digit in digit_str if digit != '.')


if __name__ == '__main__':
  getcontext().prec = 110

  total_digit_sum = 0
  for i in range(100):
    if not math.sqrt(i).is_integer():
      result = Decimal(i).sqrt()
      result = str(result)[:101]
      add = digit_sum(str(result))
      total_digit_sum += add
  print(total_digit_sum)
