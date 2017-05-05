def numbers_to_check(rang):
  """return list removing all numbers that have a multiple of themselves in the range"""
  numbers = list(rang)
  return [n for n in numbers if n*2 not in numbers][::-1]

def smallest_number_divisible_by_range(rang):
  """return the smallest positive integer that is divisible by all numbers in a range"""
  max_divisor = max(rang)
  curr_number = max_divisor
  to_check = numbers_to_check(rang)
  while True:
    for divisor in to_check:
      if not curr_number % divisor == 0:
        curr_number += max_divisor
        break
    else:
      return curr_number

if __name__ == '__main__':
  start = 1
  stop = 21
  rang = range(start, stop)
  print("The smallest positive integer that is divisible by all numbers in range({}, {}) is {}"
        .format(start, stop, smallest_number_divisible_by_range(rang)))
