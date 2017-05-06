def prime_generator(thresh):
  """returns generator for prime numbers in ascending order until thresh"""
  #erastothenes
  numbers_to_check = list(range(2, thresh))
  while numbers_to_check:
    current = numbers_to_check[0]
    yield current
    numbers_to_check = [n for n in numbers_to_check if not n % current == 0]

def nth_prime(n):
  """returns the nth prime, considering that 2 is the first"""
  #the threshold is empirical, I wonder if there is a better way?
  return list(prime_generator(120000))[n-1]

if __name__ == '__main__':
  n = 10001
  print("Prime number no {} is {}".format(n, nth_prime(n)))
