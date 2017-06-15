def is_palindrome(string):
  """return True if spelling is same left and right, False otherwise"""
  return string == string[::-1]

def is_not_lychrel_number(number_str, not_lychrel_set):
  """return True if the number is not a lychrel number, False otherwise"""
  intermediates = set()
  for _ in range(50):
    number_str = str(int(number_str) + int(number_str[::-1]))
    intermediates.add(number_str)
    if is_palindrome(number_str) or number_str in not_lychrel_set:
      not_lychrel_set.update(intermediates)
      return True

  return False

if __name__ == '__main__':
  lychrel_count = 0
  not_lychrel_set = set()
  for n in range(10000):
    if not is_not_lychrel_number(str(n), not_lychrel_set):
      lychrel_count += 1

  print("There are {} lychrel numbers below 10000".format(lychrel_count))
