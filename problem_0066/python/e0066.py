import math


def generate_non_quadratics(threshold):
  """Return generator for non quadratic integers in ascending order."""
  for i in range(1, threshold + 1):
    if not math.sqrt(i).is_integer():
      yield i


def calculate_next_fraction(n, m, d, a):
  """Return the next m, d, a."""
  next_m = d * a - m
  next_d = (n - next_m ** 2) // d
  next_a = math.floor((math.sqrt(n) + next_m) // next_d)

  return next_m, next_d, next_a


# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
def get_square_root_fractions(number):
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
      _ = fractions[1:].index(fraction) + 1
      return [fraction[2] for fraction in fractions]
    except ValueError:
      fractions.append(fraction)


def roll_up_fractions(fraction_list):
  """Return global numerator and denumenator."""
  num, den = 1, 0
  for fraction in fraction_list[::-1]:
    num, den = den, num
    num += fraction * den
  return num, den


def expand_square_root(number):
  """Return num, den for square root expansion of number."""
  fractions = get_square_root_fractions(number)
  a, fractions = fractions[0], fractions[1:]
  fraction_list = [a]
  i = 0
  while True:
    yield roll_up_fractions(fraction_list)
    fraction_list.append(fractions[i])
    i += 1
    if i == len(fractions):
      i = 0


# https://en.wikipedia.org/wiki/Pell%27s_equation#Example
def solve_quadratic_diophantine(D):
  """Return x and y integer solution of x^2 + Dy^2 = 1."""
  for num, den in expand_square_root(D):
    result = num ** 2 - D * den ** 2
    if result == 1:
      return num, den


if __name__ == '__main__':
  threshold = 1000
  non_quadratics = generate_non_quadratics(threshold)
  max_x, max_D = 0, 1
  for D in non_quadratics:
    x, y = solve_quadratic_diophantine(D)
    if x > max_x:
      max_x, max_D = x, D
    print("D: {}, x: {}, y: {}, max_D: {}".format(D, x, y, max_D))
  print("The max D is {} with an x value of {}".format(max_D, max_x))
