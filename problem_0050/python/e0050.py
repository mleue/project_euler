import time

def prime_sieve(thresh):
  """return a list of primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

if __name__ == '__main__':
  start = time.time()
  thresh = 1000000
  primes = prime_sieve(thresh)
  primes_set = set(primes)
  
  max_n, max_sum = 1, 0
  for i, _ in enumerate(primes[:5000]):
    curr_n, curr_sum = 0, 0
    while curr_sum < thresh:
      curr_sum += primes[i + curr_n]
      curr_n += 1
      if curr_sum in primes_set:
        if curr_n > max_n:
          max_n, max_sum = curr_n, curr_sum

  print("The longest sum of consecutive primes that result in a prime below {} is {} elements long and sums up to {}"
        .format(thresh, max_n, max_sum))
  print(time.time() - start)
