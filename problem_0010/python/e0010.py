from collections import OrderedDict

def prime_generator(thresh):
  """return all prime numbers up to thresh"""
  #erastothenes sieve
  #initial dict with all potential numbers marked as primes
  prime_sieve = OrderedDict()
  for n in range(2, thresh):
    prime_sieve[n] = True

  #now go through the entire dict...
  for curr in prime_sieve.keys():
    if not prime_sieve[curr]:
      continue
    #...and for every prime number we find, mark all multiples of that number as non-primes
    for n in range(curr*2, thresh, curr):
      prime_sieve[n] = False

  return [n for n, is_prime in prime_sieve.items() if is_prime]

if __name__ == '__main__':
  thresh = 2000000
  print("The sum of all prime numbers below {} is {}"
        .format(thresh, sum(prime_generator(thresh))))
