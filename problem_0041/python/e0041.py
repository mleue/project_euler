from itertools import permutations

def is_n_pandigital(number_str):
  """return True if n-digit number_str contains the digits 1 through n exactly once"""
  n = len(number_str)
  check_against = set([str(digit) for digit in range(1, n + 1)])
  return set(number_str) == check_against

def is_prime(n):
  """return True if n is prime"""
  if n % 2 == 0:
    return False
  if n % 3 == 0:
    return False

  i = 5
  w = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += w
    w = 6 - w
  return True

def find_max_pandigital_prime():
  """return the largest pandigital prime"""
  i = 9
  while i > 0:
    perm = permutations([str(digit) for digit in range(i, 0, -1)])
    for to_test in perm:
      if is_prime(int(''.join(to_test))):
        return int(''.join(to_test))
    i -= 1

if __name__ == '__main__':
  print("The largest n-pandigital prime is: {}.".format(find_max_pandigital_prime()))
