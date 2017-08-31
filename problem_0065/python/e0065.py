def generate_e_fraction_terms(n):
  """Return n fraction terms for sqrt(e)."""
  yield 2
  count = 1
  for i in range(2, n + 1):
    if i % 3 == 0:
      yield i - count
      count += 1
    else:
      yield 1


def roll_up_fractions(fraction_list):
  """Return global numerator and denumenator."""
  num, den = 1, 0
  for fraction in fraction_list[::-1]:
    num, den = den, num
    num += fraction * den
  return num, den


def sum_of_digits(number):
  """Return sum of digits of number."""
  return sum(int(digit) for digit in str(number))


if __name__ == '__main__':
  n_terms = 100
  fractions = list(generate_e_fraction_terms(n_terms))
  numerator, _ = roll_up_fractions(fractions)
  print(sum_of_digits(numerator))
