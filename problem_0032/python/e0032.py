def is_pandigital(number_str):
  """check if number_str is a pandigital number, i.e. if it has n digits,
     it must contain all numbers from 1 through n"""
  digits = [int(d) for d in number_str]
  l = len(digits)
  if set(digits) == set(range(1, l + 1)):
    return True
  else:
    return False

def check_i_j(i, j, pandigitals):
  """checks whether the product is >9999 and if not
     checks whether it is in fact a 1-9 pandigital"""
  product = i*j
  if product > 9999:
    return False
  number_str = str(i) + str(j) + str(product)
  if is_pandigital(number_str):
    pandigitals.add(product)
  return True

def check_ranges(start_i, end_i, start_j, end_j, pandigitals):
  """which ranges of potential factors to check"""
  for i in range(start_i, end_i):
    for j in range(start_j, end_j):
      if not check_i_j(i, j, pandigitals):
        break

if __name__ == '__main__':
  pandigitals = set()
  check_ranges(1, 10, 1000, 10000, pandigitals)
  check_ranges(10, 100, 100, 1000, pandigitals)

  print("The sum of all 1-9 pandigital f1,f2,product combinations is: {}"
         .format(sum(pandigitals)))
