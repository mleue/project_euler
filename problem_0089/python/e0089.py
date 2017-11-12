from config import R_TO_D, MINIMAL_ROMAN


def read_roman_numerals(filename='roman_numerals.txt'):
  """Return list of roman numerals as strings."""
  with open(filename) as f:
    return [line.strip() for line in f.readlines()]


def parse_roman(roman):
  """Return groups of consecutive chars in the roman string.

  Example:
    'XXXXVIIII' -> [['X', 4], ['V', 1], ['I', 4]]
  """
  groups = []
  curr = None
  for char in roman:
    if curr is None or curr != char:
      groups.append([char, 1])
    else:
      groups[-1][1] = groups[-1][1] + 1
    curr = char
  return groups


def convert_roman_to_decimal(roman, r_to_d):
  """Return value of roman string as a decimal integer."""
  groups = parse_roman(roman)
  decimal_sum = 0
  prev = None
  # read from right to left
  for group in groups[::-1]:
    curr_value = r_to_d[group[0]] * group[1]
    # is it an addition (i.e. higher than the group to the right)
    if prev is None or r_to_d[group[0]] > prev:
      decimal_sum += curr_value
    # or is it a subtraction
    else:
      decimal_sum -= curr_value
    prev = r_to_d[group[0]]

  return decimal_sum


def split_decimal(decimal):
  """Return list of the parts of the decimal, i.e. thousands, hundreds, etc.

  Example:
    1345 -> [1000, 300, 40, 5]
  """
  decimal_parts = []
  for i, digit in enumerate(str(decimal)[::-1]):
    if digit == '0':
      continue
    decimal_parts.append(int(digit)*(10**i))
  return decimal_parts[::-1]


def convert_decimal_to_roman(decimal, minimal_roman):
  """Return minimal roman string for this decimal."""
  decimal_parts = split_decimal(decimal)
  roman = []
  for part in decimal_parts:
    roman.append(minimal_roman[part])
  return ''.join(roman)


if __name__ == '__main__':
  assert read_roman_numerals()[-1] == 'XXXXVIIII'
  assert parse_roman('XXXXVIIII') == [['X', 4], ['V', 1], ['I', 4]]
  assert convert_roman_to_decimal('XIX', R_TO_D) == 19
  assert split_decimal(1345) == [1000, 300, 40, 5]
  assert split_decimal(1340) == [1000, 300, 40]
  assert convert_decimal_to_roman(49, MINIMAL_ROMAN) == 'XLIX'
  with open('roman_numerals_test.txt') as test_file:
    for line in test_file:
      decimal_str, roman_str = line.split()
      dec = convert_roman_to_decimal(roman_str, R_TO_D)
      assert int(decimal_str) == dec
      roman_string_minimal = convert_decimal_to_roman(dec, MINIMAL_ROMAN)
      assert roman_string_minimal == roman_str

  characters_saved = 0
  for roman_string in read_roman_numerals():
    dec = convert_roman_to_decimal(roman_string, R_TO_D)
    roman_string_minimal = convert_decimal_to_roman(dec, MINIMAL_ROMAN)
    assert len(roman_string_minimal) <= len(roman_string)
    characters_saved += len(roman_string) - len(roman_string_minimal)
  print(characters_saved)
