from itertools import permutations
import time

def prime_sieve(thresh):
  """return ordered list of primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

def prime_sieve2(n):
  """ Returns  a list of primes < n """
  sieve = [True] * n
  for i in range(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
  return [2] + [i for i in range(3,n,2) if sieve[i]]

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

def concatenate_to_prime(prime1, prime2):
  """check if the two primes concatenate to another prime in all combinations"""
  prime1_str = str(prime1)
  prime2_str = str(prime2)
  return is_prime(int(prime1_str + prime2_str)) and is_prime(int(prime2_str + prime1_str))

def get_all_combinations(prime, primes_set):
  prime_str = str(prime)
  combinations = set()
  n = 0
  if len(prime_str) > 6:
    n = len(prime_str) // 2 - 1
  for i in range(1+n, len(prime_str)-n):
    n1 = prime_str[:i]
    n2 = prime_str[i:]
    if n1[0] == '0' or n2[0] == '0':
      continue
    if int(n1) in primes_set and int(n2) in primes_set and int(n2 + n1) in primes_set:
      combinations.add(frozenset((int(n1), int(n2))))
  return combinations

if __name__ == '__main__':
  start = time.time()
  primes = prime_sieve2(100000000)
  primes_set = set(primes)
  print("{} primes in the sieve".format(len(primes)))
  print("{} seconds to run the prime sieve".format(time.time() - start))

  start = time.time()
  pairs = set()
  for prime in primes:
    pairs.update(get_all_combinations(prime, primes_set))
  print("There are {} pairs".format(len(pairs)))
  print("{} seconds to compute the pairs".format(time.time() - start))

  ##check which primes pair with each other to a concatenated prime
  #start = time.time()
  #pairs = []
  #count = 0
  #for i1, prime1 in enumerate(primes):
  #  for i2, prime2 in enumerate(primes[i1+1:], i1+1):
  #    count += 1
  #    if concatenate_to_prime(prime1, prime2):
  #      pairs.append((prime1, prime2))
  #print("There are {} pairs, checking {} combinations".format(len(pairs), count))
  #print("{} seconds to compute the pairs".format(time.time() - start))

  #build sets of partners for each prime
  start = time.time()
  prime_pairs = {prime: {prime} for prime in primes}
  for prime1, prime2 in pairs:
    prime_pairs[prime1].add(prime2)
    prime_pairs[prime2].add(prime1)
  print("{} seconds to build sets of partners".format(time.time() - start))

  triplets = set()
  for prime1, prime2 in pairs:
    concat = prime_pairs[prime1] & prime_pairs[prime2]
    if len(concat) > 2:
      for prime in concat:
        if prime != prime1 and prime != prime2:
          triplets.add(frozenset((prime1, prime2, prime)))
  print("There are {} triplets.".format(len(triplets)))

  fourlets = set()
  for prime1, prime2, prime3 in triplets:
    concat = prime_pairs[prime1] & prime_pairs[prime2] & prime_pairs[prime3]
    if len(concat) > 3:
      for prime in concat:
        if prime != prime1 and prime != prime2 and prime != prime3:
          fourlets.add(frozenset((prime1, prime2, prime3, prime)))
  print("There are {} fourlets.".format(len(fourlets)))

  fivelets = set()
  for prime1, prime2, prime3, prime4 in fourlets:
    concat = prime_pairs[prime1] & prime_pairs[prime2] & prime_pairs[prime3] & prime_pairs[prime4]
    if len(concat) > 4:
      for prime in concat:
        if prime != prime1 and prime != prime2 and prime != prime3 and prime != prime4:
          fivelets.add(frozenset((prime1, prime2, prime3, prime4, prime)))
  print("There are {} fivelets.".format(len(fivelets)))
  print(fivelets)
