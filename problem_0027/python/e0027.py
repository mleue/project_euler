from collections import OrderedDict

def generate_primes(thresh):
  """generate all primes below thresh"""
  is_prime = OrderedDict({n: True for n in range(2, thresh)})
  for number in is_prime.keys():
    if not is_prime[number]:
      continue
    #remove all multiples from the sieve
    for n in range(number*2, thresh, number):
      is_prime[n] = False

  return set((n for n, is_p in is_prime.items() if is_p))

def quadratic_primes(a, b, primes):
  """return how many consecutive primes can be created by n**2 + a*n + b"""
  n = 0
  while True:
    value = n**2 + a*n + b
    if value in primes:
      n += 1
    else:
      return n

if __name__ == '__main__':
  max_quadratic_primes = 0
  a_max, b_max = None, None
  primes = generate_primes(100000)

  for b in range(-1000, 1001):
    #since the equation is n**2 + a*n + b, b has to be a prime in order for the first output (n==0)
    #to be a prime, therefore we can hop over all choices for b that are not primes
    if b not in primes:
      continue
    for a in range(-999, 1000):
      curr_quadratic_primes = quadratic_primes(a, b, primes)
      if max_quadratic_primes < curr_quadratic_primes:
        max_quadratic_primes = curr_quadratic_primes
        a_max, b_max = a, b

  print(a_max * b_max)
