def is_divisible_by(dividend, divisor):
  """return True if divisible, False if not"""
  return dividend % divisor == 0

def prime_numbers(max_thresh):
  """create prime numbers below a max threshold"""
  #sieve of erastothenes
  to_check = list(range(2, max_thresh))
  while to_check:
    current_prime = to_check[0]
    yield current_prime
    to_check = [n for n in to_check if not is_divisible_by(n, current_prime)] 

def largest_prime_factor(number):
  """return the largest prime factor of the given number"""
  for prime in prime_numbers(10000):
    if is_divisible_by(number, prime):
      number //= prime
      if number == 1:
        return prime

if __name__ == '__main__':
  number = 600851475143
  print("The largest prime factor of {} is {}".format(number, largest_prime_factor(number)))
