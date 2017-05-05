import math

def is_palindromic(number):
  """return True if number is palindromic, False if not"""
  if not isinstance(number, int):
    raise TypeError("Only integers can be checked.")
  if number < 0:
    raise ValueError("Only positive integers can be checked.")

  number_str = str(number)
  return number_str[::-1] == number_str

def create_palindromic_numbers(start_max):
  """return generator for palindromic numbers in descending order"""
  n = start_max
  while n > -1:
    if is_palindromic(n):
      yield n
    n -= 1

def get_number_of_digits(number):
  """return the number of digits of a number"""
  return int(math.log10(number))+1

def is_product_of_two_n_digit_numbers(number, digits):
  """returns whether number is the product of two numbers with n digits"""
  check_interval = range((10**digits)-1, 10**(digits-1), -1)
  for factor1 in check_interval:
    #check if the number is divisible by factor1
    if number % factor1 == 0:
      factor2_digits = get_number_of_digits(number/factor1)
      #does factor2 have as many digits as factor1? then we have a match
      if factor2_digits == digits:
        return True
      #is factor1 so small that factor2 now has more digits than factor1? then we can break
      elif factor2_digits > digits:
        break
  return False

def largest_palindromic_number_as_product(digits):
  """return largest palindromic number that is the product of two digits long numbers"""
  start_max = (10**digits) * (10**digits)
  for palindromic_number in create_palindromic_numbers(start_max):
    if is_product_of_two_n_digit_numbers(palindromic_number, digits):
      return palindromic_number
  return None

if __name__ == '__main__':
  digits = 3
  print("The largest palindromic number that is the product of two {} digit numbers is {}."
        .format(digits, largest_palindromic_number_as_product(digits)))
