import math
from factorize import get_prime_factors


def get_closest_lower_proper_fraction_to_k(prime_factors, thresh, k=3/7):
  """Return num, den of closest lower proper fraction to k."""
  # starting with the known start values given in the problem description
  max_num, max_den = 2, 5
  max_value = max_num / max_den
  for d in range(8, thresh+1):
    # creating a range of possible n values to check based on the
    # remaining solution range for n delimited to the left by
    # d*(currently best solution) and to the right by d*k
    min_n = math.floor(d*max_value)
    max_n = math.ceil(d*k)
    for n in range(min_n, max_n):
      # when their gcd is 1, i.e. it is a proper fraction
      if not set.intersection(set(prime_factors[n]), set(prime_factors[d])):
        curr_value = n/d
        if curr_value < k and curr_value > max_value:
          max_value, max_num, max_den = curr_value, n, d

  return max_num, max_den


if __name__ == '__main__':
  threshold = 1000000
  n_to_prime_factors = get_prime_factors(threshold)
  print(get_closest_lower_proper_fraction_to_k(n_to_prime_factors, threshold))
