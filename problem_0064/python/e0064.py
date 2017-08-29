import math


def calculate_next_fraction(n, m, d, a):
  """Return the next m, d, a."""
  next_m = d * a - m
  next_d = (n - next_m ** 2) // d
  next_a = math.floor((math.sqrt(n) + next_m) // next_d)

  return next_m, next_d, next_a


# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
def get_square_root_fraction_period(number):
  """Return the fraction period for the continued fraction of n."""
  if math.sqrt(number).is_integer():
    return 0

  m, d, a = 0, 1, math.floor(math.sqrt(number))
  fractions = [(m, d, a)]
  iteration = 0
  while True:
    iteration += 1
    fraction = calculate_next_fraction(number, *fractions[-1])
    try:
      index = fractions[1:].index(fraction) + 1
      return iteration - index
    except ValueError:
      fractions.append(fraction)


def period_is_odd(p):
  """Return True if odd, False otherwise."""
  return not p % 2 == 0


if __name__ == '__main__':
  sum_odd_periods = 0
  threshold = 10001
  for i in range(1, threshold):
    period = get_square_root_fraction_period(i)
    if period_is_odd(period):
      sum_odd_periods += 1

  print(sum_odd_periods)
