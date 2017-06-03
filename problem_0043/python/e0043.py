from itertools import permutations

def check_divisibility(number_str, check_ranges):
  """return True if number_str can be divided in all check_ranges
     a check range is a tuple (substr_start, substr_end, divisor)"""
  for substr_start, substr_end, divisor in check_ranges:
    #-1 because the given ranges are 1-based
    if int(number_str[(substr_start-1) : substr_end]) % divisor != 0:
      return False
  return True

if __name__ == '__main__':
  pandigitals = permutations((str(d) for d in range(10)))
  check_ranges = ((8, 10, 17), (7, 9, 13), (6, 8, 11), (5, 7, 7), (4, 6, 5), (3, 5, 3), (2, 4, 2))
  pandigital_sum = 0
  for pandigital in pandigitals:
    if check_divisibility(''.join(pandigital), check_ranges):
      pandigital_sum += int(''.join(pandigital))

  print("The sum of all 0-9 pandigitals with the given properties is {}".format(pandigital_sum))
