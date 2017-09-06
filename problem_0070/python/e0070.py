from factorize import get_prime_factors


# https://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
def calc_phi(n, factors):
  """Return eulers totient (or phi function) for the given prime factors."""
  product = n
  for factor in set(factors):
    product *= 1 - (1 / factor)
  return int(product)


def is_permutation(n1, n2):
  """Return True if n1 and n2 are permutations of each other, False if not."""
  return sorted(list(str(n1))) == sorted(list(str(n2)))


def get_min_n_over_phi_permutation(prime_factors):
  """Return the maximum n over phi for all numbers and their prime factors."""
  min_n_over_phi_permutation, min_n = 10, 0
  for n, factors in prime_factors.items():
    if n < 10:
      continue
    phi = calc_phi(n, factors)
    if is_permutation(n, phi):
      n_over_phi = n / phi
      if n_over_phi < min_n_over_phi_permutation:
        min_n_over_phi_permutation, min_n = n_over_phi, n
  return min_n_over_phi_permutation, min_n


if __name__ == '__main__':
  threshold = 10000000
  n_to_prime_factors = get_prime_factors(threshold)
  result, number = get_min_n_over_phi_permutation(n_to_prime_factors)
  print("""The minimum n/phi (with n and phi being permutations)
         for all n <= {} is {} at {}"""
        .format(threshold, result, number))
