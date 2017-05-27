import math

base2_lookup = {d: 2**d for d in range(50)}

def dec_to_base2(number_dec):
  """convert from dec to base2"""
  n_digits = math.floor(math.log2(number_dec)) + 1
  rest = number_dec
  number_base2 = ['0']*n_digits
  for d in reversed(range(n_digits)):
    if base2_lookup[d] <= rest:
      number_base2[d] = '1'
      rest -= base2_lookup[d]

  return ''.join(number_base2)

def is_palindromic(number_str):
  """return True if number_str is a palindrome"""
  if number_str[0] == '0':
    return False
  else:
    return number_str == number_str[::-1]

if __name__ == '__main__':
  thresh = 1000000
  sum_double_palindromes = 0
  for n in range(1, thresh):
    if is_palindromic(str(n)) and is_palindromic(dec_to_base2(n)):
      sum_double_palindromes += n
  print("The sum of all double palindromic numbers below {} is {} ."
        .format(thresh, sum_double_palindromes))
