from itertools import combinations
from factorize import get_prime_factors, primes_set


def sum_is_odd(d, n):
  """Return True if sum of d and n is odd, False otherwise."""
  return (d + n) % 2 == 1


def reduced_odd_fractions(prime_factors, thresh):
  """Return reduced odd (i.e. num+den=odd) fractions with den <= thresh."""
  reduced_fractions = []
  for d in range(2, thresh+1):
    if d in primes_set:
      for n in range(1, d):
        if sum_is_odd(d, n):
          reduced_fractions.append((n, d))
    else:
      for n in range(1, d):
        if sum_is_odd(d, n):
          if not set.intersection(prime_factors[d], prime_factors[n]):
            reduced_fractions.append((n, d))

  return reduced_fractions


# https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
def pythagorean_triplet(n, m):
  """Return a, b and c of the pythagorean triplet."""
  a = m**2 - n**2
  b = 2*m*n
  c = m**2 + n**2
  return a, b, c


if __name__ == '__main__':
  threshold = 1000
  n_to_factors = get_prime_factors(threshold)
  n_to_factors[1] = [1]
  n_to_factors = {n: set(factors) for n, factors in n_to_factors.items()}
  fractions = reduced_odd_fractions(n_to_factors, threshold)

  maximum = 1500000
  counter = {L: 0 for L in range(5, maximum+1)}
  for n, m in fractions:
    a, b, c = pythagorean_triplet(n, m)
    circumference = a+b+c
    factor = 1
    while circumference*factor <= maximum:
      counter[circumference*factor] = counter[circumference*factor] + 1
      factor += 1

  single_solution = [L for L, count in counter.items() if count == 1]
  print(single_solution[-20:])
  print(single_solution[:20])
  print(len(single_solution))

# the strategy:
# - for every .../d:
#   - generate all proper n/d fractions (n < d) (see e0072)
# - use these n/d to generate pythagorean triplets according to euler's formula
#   https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
# - add a, b, c of each triplet to get the circumference and count the number of
#   appearances of each circumference
# - generating triplets using euler's formula will not create multiples like
#   e.g. (6, 8, 10) being the integer multiple of (3, 4, 5), so to get all
#   number of ways to create a particular circumference we multiply created ones
#   up to <= the maximum circumference threshold
# - from the counter, grab all those that have a unique appearance (count == 1)
