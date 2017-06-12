def get_digits_set(number):
  """get set of char digits of number"""
  return set((d for d in str(number)))

def is_2x_to_6x_permutable(number):
  """check if all numbers 2x, 3x, 4x, 5x, 6x contain the same digits as number"""
  digits_set = get_digits_set(number)
  multipliers = (2, 3, 4, 5, 6)
  for m in multipliers:
    if not get_digits_set(m*number) == digits_set:
      return False

  return True

def find_smallest_2x_to_6x_permutable():
  """return the smallest integer whose 2x, 3x, 4x, 5x, and 6x all contain
     the same digits as the number itself"""
  lower_thresh, upper_thresh = 10, 17
  while True:
    for n in range(lower_thresh, upper_thresh):
      if is_2x_to_6x_permutable(n):
        return n

    lower_thresh *= 10
    upper_thresh *= 10

if __name__ == '__main__':
  print(find_smallest_2x_to_6x_permutable())
