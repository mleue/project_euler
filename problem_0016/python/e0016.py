def digit_sum(n):
  """sum up n's digits"""
  return sum((int(digit) for digit in str(n)))

if __name__ == '__main__':
  n = 2**1000
  print("The sum of the digits of {} is {}"
        .format(n, digit_sum(n)))
