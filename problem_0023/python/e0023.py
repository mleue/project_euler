import time
import math

def proper_divisors(n):
  """return a set of the divisors of n that divide it without rest and < n"""
  divisors = {1}
  #f1*f2 = n, any f1 can at max be sqrt(n), so we can stop there
  for factor1 in range(2, math.floor(math.sqrt(n))+1):
    if n % factor1 == 0:
      factor2 = n // factor1
      divisors.add(factor1)
      divisors.add(factor2)

  return divisors

def is_abundant(n):
  """return True if sum(proper_divisors(n)) > n"""
  return sum(proper_divisors(n)) > n

def not_sum_of_two_abundant_numbers_below_thresh(thresh):
  """returns list of all numbers below the threshold that can not be expressed 
     as the sum of two abundant numbers"""
  start = time.time()
  abundant_numbers = [n for n in range(2, thresh) if is_abundant(n)]
  check_sum_of_two_abundant = {n: False for n in range(1, thresh+1)}

  #this can probably be done faster utilizing that abundant_numbers is sorted
  #binary search maybe?
  for n in abundant_numbers:
    for m in abundant_numbers:
      s = n+m
      if m > n or s > thresh:
        break
      else:
        check_sum_of_two_abundant[s] = True
  print("It took {:.3f} s".format(time.time() - start))

  return [number for number, pred in check_sum_of_two_abundant.items() if not pred]


if __name__ == '__main__':
  thresh = 28123
  print("The sum of all numbers below {} that are not the sum of two abundant numbers is {}"
        .format(thresh, sum(not_sum_of_two_abundant_numbers_below_thresh(thresh))))
