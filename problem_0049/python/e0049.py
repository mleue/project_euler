from itertools import permutations

def prime_sieve(thresh):
  """return a list of primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

if __name__ == '__main__':
  lower_thresh = 999
  upper_thresh = 10000
  dist = 3330

  primes = [prime for prime in prime_sieve(upper_thresh) if prime > lower_thresh]
  primes_set = set(primes)

  for prime in primes:
    hits = [prime]
    unique_int_permutations = set((int(''.join(perm)) for perm in permutations(str(prime))))
    for n in unique_int_permutations:
      if n in primes_set:
        hits.append(n)

    if len(hits) >= 3:
      control1 = hits[0] + dist
      control2 = hits[0] + 2*dist
      if control1 in hits and control2 in hits:
        print(hits[0], control1, control2)
