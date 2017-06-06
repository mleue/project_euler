def prime_sieve(thresh):
  """return list of primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

def odd_composite_numbers(factor_thresh):
  """return list of odd composite numbers"""
  numbers_set = set()
  for i in range(3, factor_thresh):
    for j in range(i, factor_thresh):
      curr = i*j
      if curr % 2 == 1:
        numbers_set.add(i*j)

  return sorted(list(numbers_set))

def check_conjecture(composite_number, primes, double_squares):
  """check a composite number, return True if it holds the Goldbach conjecture"""
  for p in primes:
    for s in double_squares:
      curr = p + s
      if curr == composite_number:
        return True
      elif curr > composite_number:
        break

  return False

if __name__ == '__main__':
  thresh = 10000
  factor_thresh = 500
  composite_numbers = odd_composite_numbers(factor_thresh)

  primes = prime_sieve(thresh)
  double_squares = [2 * n**2 for n in range(1, 100)]

  for n in composite_numbers:
    if not check_conjecture(n, primes, double_squares):
      print("The first odd composite number to violate the Goldbach conjecture is {}".format(n))
      break
