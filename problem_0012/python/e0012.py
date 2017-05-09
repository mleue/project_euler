def triangle_number_generator():
  """generate triangle numbers"""
  to_add = 1
  curr = 0
  while True:
    curr += to_add
    to_add += 1
    yield curr

def number_of_divisors(number):
  """return number of divisors for provided number"""
  #the largest divisor for any number (besides from itself) can be at max number//2
  thresh = number//2
  divisors = set()
  for check_divisor in range(1, thresh):
    mod = number % check_divisor
    #every successful integer division gives us information about two divisors (factor1 * factor2 = number)
    if mod == 0 and check_divisor not in divisors:
      #add both
      divisors.add(check_divisor)
      divisors.add(number//check_divisor)
    #at some point we will simply start checking divisors that are the flipped version of ones we checked before
    #(e.g. 120/12 = 10, 120/10 = 12), at that point we know we have all of them and can break and return
    elif check_divisor in divisors:
      break

  return len(divisors)

def triangle_number_more_than_n_divisors(n):
  """return the first triangle number with more than n divisors"""
  for triangle_number in triangle_number_generator():
    if number_of_divisors(triangle_number) > n:
      return triangle_number

if __name__ == '__main__':
  n = 500
  print("The first triangle number with more than {} divisors is {}"
        .format(n, triangle_number_more_than_n_divisors(n)))
