from itertools import permutations

def primes_below_thresh(thresh):
  """generator for primes below threshold"""
  primes_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if primes_lookup[n]:
      for tick_off in range(n+n, thresh, n):
        primes_lookup[tick_off] = False

  return sorted((n for n, is_prime in primes_lookup.items() if is_prime))

def get_rotations(number_str):
  """get all rotations, e.g. 197 -> 197, 971, 719"""
  for i in range(len(number_str)):
    yield number_str[i:]+number_str[:i]

def number_of_circular_primes(prime_list):
  """return the number of circular primes in the list of primes"""
  prime_str_list = [str(prime) for prime in prime_list]
  prime_str_set = set(prime_str_list)
  count = 0
  for prime_str in prime_str_list:
    if all((rotation in prime_str_set for rotation in get_rotations(prime_str))):
      #print(prime_str[::-1])
      count += 1

  return count

if __name__ == '__main__':
  thresh = 1000000
  print("The number of circular primes below {} is {}"
        .format(thresh, number_of_circular_primes(primes_below_thresh(thresh))))
