from collections import Counter, deque

prime_factors_lookup = {1: [1]}
def prime_factors(number, primes, prime_set):
  """return list of the prime factors of number"""
  if number in prime_factors_lookup:
    return prime_factors_lookup[number]
  elif number in prime_set:
    return [1]

  prime_factors = []
  curr = number
  while curr != 1:
    if curr in prime_factors_lookup:
      prime_factors.extend(prime_factors_lookup[curr])
      break
    for prime in primes:
      if curr % prime == 0:
        prime_factors.append(prime)
        curr //= prime
        break
  prime_factors_lookup[number] = prime_factors
  return prime_factors

def prime_sieve(thresh):
  """return list of all primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

def combine_same(number_list):
  """return a set of numbers based on number_list with all duplicates combined"""
  number_counter = Counter(number_list)
  return set((n*count for n, count in number_counter.items()))

def consecutive_distinct_prime_factors(n):
  """return first number of n consecutive numbers with n distinct primes each"""
  primes = prime_sieve(150000)
  prime_set = set(primes)
  queue = deque([combine_same(prime_factors(i, primes, prime_set)) for i in range(2, 4)], maxlen=n)
  curr = 2
  while True:
    if curr % 10000 == 0:
      print(curr)
    queue.append(combine_same(prime_factors(curr + n - 1, primes, prime_set)))
    distinct_prime_factors = set((prime_factor for prime_factors in queue for prime_factor in prime_factors))
    if len(distinct_prime_factors) >= n*n:
      return curr
    curr += 1

if __name__ == '__main__':
  print(consecutive_distinct_prime_factors(4))
