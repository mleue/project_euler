from itertools import permutations

def prime_sieve(thresh):
  """return ordered list of primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

def is_prime(n):
  """return True if n is prime"""
  if n % 2 == 0:
    return False
  if n % 3 == 0:
    return False

  i = 5
  w = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += w
    w = 6 - w
  return True

def concatenate_to_prime(known, candidate, primes_set):
  """check if candidate concatenates with all knowns to a prime"""
  candidate_str = str(candidate)
  for known_prime in known:
    known_prime_str = str(known_prime)
    concat1 = int(known_prime_str + candidate_str)
    if concat1 in primes_set or is_prime(concat1):
      pass
    else:
      return False
    concat2 = int(candidate_str + known_prime_str)
    if concat2 in primes_set or is_prime(concat2):
      pass
    else:
      return False

  return True

if __name__ == '__main__':
  primes = prime_sieve(700)
  primes_set = set(primes)
  #print(concatenate_to_prime([3, 7, 109], 673, primes_set))
  pairs = []
  for i1, prime1 in enumerate(primes):
    for i2, prime2 in enumerate(primes[i1+1:], i1+1):
      if concatenate_to_prime([prime1], prime2, primes_set):
        pairs.append((prime1, prime2))
  print(len(pairs))
  prime_pairs = {prime: {prime} for prime in primes}
  for pair in pairs:
    prime_pairs[pair[0]].add(pair[1])
    prime_pairs[pair[1]].add(pair[0])
  #print(prime_pairs)
  test = set()
  for prime in prime_pairs[3]:
    test.update(prime_pairs[prime])
  print(test)
  print(3, [prime_pairs[prime] for prime in prime_pairs[3]])
  print(7, prime_pairs[7])
  print(109, prime_pairs[109])
