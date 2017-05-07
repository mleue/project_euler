import re
import functools

def import_number_string(filename):
  """import the 1000 digit number for this question from file as a string"""
  with open(filename, 'r', encoding='utf-8') as f:
    return re.sub(r'[^\d]', '', f.read())

def all_n_char_substrings(string, n):
  """returns generator for all n-char substrings of string"""
  for i in range(len(string) - n + 1):
    yield string[i:i+n]

def greatest_adjacent_product(number_str, n):
  """return the greatest product of n adjacent digits from a number in string form"""
  greatest = 0
  for n_char_substring in all_n_char_substrings(number_str, n):
    current = functools.reduce(lambda x, y: int(x)*int(y), n_char_substring)
    greatest = current if current > greatest else greatest
  return greatest

if __name__ == '__main__':
  string, n = import_number_string('number.txt'), 13
  print("The value of the greatest product of {} adjacent digits in the 1000 digit string is: {}"
        .format(n, greatest_adjacent_product(string, n)))
