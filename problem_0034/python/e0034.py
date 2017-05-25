#factorial(9) = 362880
#so every digit can at max add 362880
#so the highest possible number is ~2mio

def factorial(n):
  """recursive factorial calculation !n"""
  if n == 0:
    return 1
  elif n == 1:
    return n
  else:
    return n*factorial(n-1)

def sum_curious_numbers(thresh):
  """return the sum of all curious numbers below thresh"""
  factorial_lookup = {n: factorial(n) for n in range(10)}
  print(factorial_lookup)
  curious_sum = 0
  for n in range(10, thresh):
    if n == sum((factorial_lookup[int(d)] for d in str(n))):
      print(n)
      curious_sum += n
  return curious_sum

if __name__ == '__main__':
  thresh = 2000000
  print("The sum of all curious numbers is {}"
        .format(sum_curious_numbers(thresh)))
