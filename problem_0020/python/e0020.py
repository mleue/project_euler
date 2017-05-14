def factorial(n):
  """return !n"""
  if n == 1:
    return n
  else:
    return n * factorial(n-1)

def sum_of_digits(n):
  """returns the sum of the digits of n"""
  return sum([int(digit) for digit in str(n)])

if __name__ == '__main__':
  n = 100
  print("The sum of the digits of the factorial !{} is {}"
        .format(n, sum_of_digits(factorial(n))))
