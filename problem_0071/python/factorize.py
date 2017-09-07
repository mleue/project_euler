from primes import prime_sieve

primes = prime_sieve(1000000)
primes_set = set(primes)


# TODO faster factorization?
def factorize(n, prime_factors):
  """Return list of prime factors of n."""
  # if n is a prime, return itself
  if n in primes_set:
    return [n]

  factors = []
  prime_index, stop = 0, n//2
  # continously divide n by the lowest clean divisor we can find
  while n > 1 and primes[prime_index] <= stop:

    if n % primes[prime_index] == 0:
      factors.append(primes[prime_index])
      n //= primes[prime_index]
      prime_index = 0

    # if any of the sub results are a number we already know the prime
    # factors for, then simply add those and break the loop
    if prime_factors[n]:
      factors.extend(prime_factors[n])
      break

    prime_index += 1

  return factors


def get_prime_factors(threshold):
  """Return dict of all prime factors for all n <= thresh."""
  prime_factors = {n: [] for n in range(2, threshold+1)}
  for j in range(2, threshold+1):
    factors = factorize(j, prime_factors)
    prime_factors[j].extend(factors)
    if j % 100000 == 0:
      print(j)
  return prime_factors
