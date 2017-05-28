#the trick is to realize that even for growing numbers, they can only be
#truncatable primes if the lower digits also are truncatable primes,
#so once you know all truncatable primes in the xx range, you know that those
#have to be the base for all larger truncatable primes
# e.g. 79, being the base for 379
#that way you can cut down on the number of potential truncatable primes and
#eventually reach a stop condition

def primes_below_thresh(thresh):
  """generator for primes below threshold"""
  primes_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if primes_lookup[n]:
      for tick_off in range(n+n, thresh, n):
        primes_lookup[tick_off] = False

  return sorted((n for n, is_prime in primes_lookup.items() if is_prime))

def is_left_right_truncatable(number_str, prime_str_set):
  """return True if the number_str can be truncated from both left and right
     and always be prime, e.g. 3797"""
  l = len(number_str)
  #left truncatable?
  for i in range(l):
    if number_str[i:] not in prime_str_set or number_str[:l-i] not in prime_str_set:
      return False
  return True

if __name__ == '__main__':
  thresh = 1000000
  prime_str_set = set([str(prime) for prime in primes_below_thresh(thresh)])
  sum_truncatable_primes = 0
  for n in range(10, thresh):
    if is_left_right_truncatable(str(n), prime_str_set):
      sum_truncatable_primes += n
  print("The sum of all left-right truncatable primes is {} ."
        .format(sum_truncatable_primes))
