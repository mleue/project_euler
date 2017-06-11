from collections import Counter

def prime_sieve(thresh):
  """return ordered list of primes below thresh"""
  is_prime_lookup = {n: True for n in range(2, thresh)}
  for n in range(2, thresh):
    if is_prime_lookup[n]:
      for i in range(n+n, thresh, n):
        is_prime_lookup[i] = False

  return sorted((n for n, is_prime in is_prime_lookup.items() if is_prime))

def get_reoccuring_digit(number, n):
  """get n times reoccuring digit from number"""
  digit_counts = Counter(str(number))
  for digit, count in digit_counts.items():
    if count == n:
      return int(digit)

  return None

def create_number_variations(number, reoccuring_digit):
  """return list of potential variations of the number and its reoccuring digit"""
  variations = []
  digit_c = str(reoccuring_digit)
  for i in range(10):
    variation = int(str(number).replace(digit_c, str(i)))
    if len(str(variation)) == len(str(number)):
      variations.append(variation)

  return variations

if __name__ == '__main__':
  thresh = 1000000
  primes = prime_sieve(thresh)
  primes_set = set(primes)
  target_count = 8
  n_reoccuring = 3

  for prime in primes:
    reoccuring_digit = get_reoccuring_digit(prime, n_reoccuring)
    if reoccuring_digit:
      variations = create_number_variations(prime, reoccuring_digit)
      count = 0
      for variation in variations:
        if variation in primes_set:
          count += 1
      if count >= target_count:
        print(variations)
        break
