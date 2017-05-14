def proper_divisors(n):
  """return set of proper divisors of n"""
  divisors = {1}
  for factor1 in range(2, n//2):
    #every divisor gives us information about two factors n = f1*f2
    #so once we have come so far along that we start seeing the first f2 again,
    #we break
    if factor1 in divisors:
      break
    elif n % factor1 == 0:
      factor2 = n // factor1
      divisors.add(factor1)
      divisors.add(factor2)

  return divisors

def is_amicable_pair(a, b, lookup):
  """return if a and b are an amicable pair according to the lookup"""
  return lookup.get(b, None) == a and a != b

def sum_of_amicable_numbers_below_n(n):
  """return the sum of amicable numbers below n"""
  n_divsum_lookup = dict()
 
  #range(n) is enough because at least one of the numbers in any pair
  #has to be below n to be able to consider the pair
  for n in range(n):
    n_divsum_lookup[n] = sum(proper_divisors(n))

  amicable_numbers = set()
  for number, div_sum in n_divsum_lookup.items():
    if is_amicable_pair(number, div_sum, n_divsum_lookup):
      amicable_numbers.add(number)
      amicable_numbers.add(div_sum)

  return sum(amicable_numbers)


if __name__ == '__main__':
  n = 10000
  print("The sum of all amicable numbers below {} is {}"
        .format(n, sum_of_amicable_numbers_below_n(n)))
