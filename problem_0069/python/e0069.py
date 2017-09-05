def prime_sieve(n):
  """Return a list of primes < n."""
  sieve = [True] * n
  for i in range(3, int(n**0.5)+1, 2):
    if sieve[i]:
      sieve[i*i::2*i] = [False] * ((n-i*i-1) // (2*i)+1)
  return [2] + [i for i in range(3, n, 2) if sieve[i]]


primes = prime_sieve(1000000)
primes_set = set(primes)


def factorize(n, prime_factors):
  """Return list of prime factors of n."""
  if n in primes_set:
    return [n]
  factors = []
  prime_index, stop = 0, n//2
  while n > 1 and primes[prime_index] < stop:
    if prime_factors[n]:
      factors.extend(prime_factors[n])
      break
    if n % primes[prime_index] == 0:
      factors.append(primes[prime_index])
      n //= primes[prime_index]
      prime_index = 0
    prime_index += 1
  return factors


# https://en.wikipedia.org/wiki/Euler's_totient_function#Euler.27s_product_formula
def calc_phi(n, factors):
  """Return eulers totient (or phi function) for the given prime factors."""
  product = n
  for factor in set(factors):
    product *= 1 - (1 / factor)
  return int(product)


def create_prime_factors(thresh):
  """Return dict of all prime factors for all n <= thresh."""
  prime_factors = {n: [] for n in range(2, threshold+1)}
  for j in range(2, threshold+1):
    factors = factorize(j, prime_factors)
    prime_factors[j].extend(factors)
    if j % 100000 == 0:
      print(j)
  return prime_factors


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
  n_to_prime_factors = create_prime_factors(threshold)
  result, number = get_max_n_over_phi(n_to_prime_factors)
  print("The maximum n/phi for all n <= {} is {} at {}"
        .format(threshold, result, number))
