def is_1_to_9_pandigital(number_str):
  """return True if the number_str is 1-9 pandigital, False otherwise"""
  if len(number_str) != 9 or '0' in number_str:
    return False
  else:
    return len(number_str) == len(set(number_str))

def check_integer(number):
  """check if number can be product concatenated to be 1-9 pandigital"""
  number_str = str(number)
  factor = 2
  while len(number_str) < 9:
    number_str += str(number * factor)
    factor += 1

  if is_1_to_9_pandigital(number_str):
    return number_str
  else:
    return None

#we only have to test integers until 9999 because after that,
#concat(i*1, i*2) would already be 10digits and thus too many
if __name__ == '__main__':
  thresh = 9999
  max_number = '0'
  for n in range(thresh):
    concat_product = check_integer(n)
    if concat_product and concat_product > max_number:
      max_number = concat_product
  print("The maximum concat product is {} .".format(max_number))
