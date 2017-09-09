from itertools import combinations
from factorize import get_prime_factors, primes_set


def calc_product(*args):
  """Return product of args."""
  product = 1
  for arg in args:
    product *= arg
  return product


def number_of_reduced_fractions(prime_factors, thresh):
  """Return number of reduced fractions with denumenator <= thresh."""
  amount = 0
  for d in range(2, thresh+1):
    if d in primes_set:
      amount += d-1
    else:
      invalid = 0
      for factor in prime_factors[d]:
        invalid += (d//factor - 1)
      for r in range(2, len(prime_factors[d])+1):
        for comb in combinations(prime_factors[d], r):
          if r % 2 == 0:
            invalid -= (d//calc_product(*comb) - 1)
          else:
            invalid += (d//calc_product(*comb) - 1)
      amount += d - invalid - 1

  return amount


if __name__ == '__main__':
  threshold = 1000000
  n_to_factors = get_prime_factors(threshold)
  n_to_factors = {n: set(factors) for n, factors in n_to_factors.items()}
  print(number_of_reduced_fractions(n_to_factors, threshold))

# the strategy:
# - for every .../d:
#   - if it is a prime:
#     - add d-1 to the number of fractions because every n[1,d-1] will work
#     - add that amount to the total amount
#   - otherwise:
#       (we calculate the number of reducable fractions for n < d
#       and subtract those from d)
#     - grab the prime factors set for d, e.g. 60: [2, 3, 5]
#     - for each of those factors:
#       - calc the number of multiples < d, i.e. d//factor - 1 and add to
#         invalids
#       - since some n can be the multiple of different factors or even
#         combinations of them, i.e. for d=60, n=30 can stem from 2, 3, 5 and
#         even combinations thereof, i.e. 6(=2*3), 10(=2*5), 15(=3*5)
#       - since we must not count those n that can stem from different factors
#         multiple times we have to be smart about calculating all combinations
#         and adding/subtracting from the invalid count
#     - now that we have a count over all invalid n < d, the number of reduced
#       proper fractions is simply d - invalids - 1
#     - add that amount to the total amount
