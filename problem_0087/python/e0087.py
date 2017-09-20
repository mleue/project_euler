from math import sqrt, ceil
from primes import prime_sieve

if __name__ == '__main__':
  thresh = 50000000
  primes = prime_sieve(ceil(sqrt(thresh)))

  valid_set = set()
  for a in primes:
    # print(a)
    a_square = a*a
    for b in primes:
      b_cubic = b*b*b
      if a_square + b_cubic >= thresh:
        break
      for c in primes:
        c_quart = c*c*c*c
        if a_square + b_cubic + c_quart >= thresh:
          break
        else:
          valid_set.add(a_square + b_cubic + c_quart)

  print(len(valid_set))
