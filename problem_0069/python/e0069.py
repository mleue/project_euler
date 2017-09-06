from factorize import get_prime_factors


# https://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
def calc_phi(n, factors):
  """Return eulers totient (or phi function) for the given prime factors."""
  product = n
  for factor in set(factors):
    product *= 1 - (1 / factor)
  return int(product)


def get_max_n_over_phi(prime_factors):
  """Return the maximum n over phi for all numbers and their prime factors."""
  max_n_over_phi, max_n = 0, 0
  for n, factors in prime_factors.items():
    phi = calc_phi(n, factors)
    n_over_phi = n / phi
    if n_over_phi > max_n_over_phi:
      max_n_over_phi, max_n = n_over_phi, n
  return max_n_over_phi, max_n


if __name__ == '__main__':
  threshold = 1000000
  n_to_prime_factors = get_prime_factors(threshold)
  result, number = get_max_n_over_phi(n_to_prime_factors)
  print("The maximum n/phi for all n <= {} is {} at {}"
        .format(threshold, result, number))
