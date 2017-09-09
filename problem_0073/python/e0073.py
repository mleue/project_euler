import math
from factorize import get_prime_factors


def proper_fractions_in_interval(prime_factors, thresh, min_frac, max_frac):
  """Return number of proper fractions between min_frac and max_frac."""
  min_value = min_frac[0]/min_frac[1]
  max_value = max_frac[0]/max_frac[1]
  amount = 0
  for d in range(2, thresh+1):
    # creating a range of possible n values to check based on the
    # min and max frac interval
    min_n = math.floor(d*min_value)
    max_n = math.ceil(d*max_value)
    for n in range(min_n, max_n):
      if n < 2:
        continue
      # when their gcd is 1 it is a proper fraction
      if not set.intersection(set(prime_factors[n]), set(prime_factors[d])):
        curr_value = n/d
        if curr_value > min_value and curr_value < max_value:
          amount += 1

  return amount


if __name__ == '__main__':
  threshold = 12000
  n_to_prime_factors = get_prime_factors(threshold)
  print(proper_fractions_in_interval(n_to_prime_factors, threshold,
                                     min_frac=(1, 3), max_frac=(1, 2)))
