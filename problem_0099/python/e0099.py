from math import log


def read_exponentials(filename='exponentials.txt'):
  """Read and yield the exponentials."""
  with open(filename) as f:
    for line in f:
      base_str, exponent_str = line.split(',')
      yield int(base_str), int(exponent_str)


if __name__ == '__main__':
  max_exponential, max_i = 0, 0
  for i, ret in enumerate(read_exponentials(), 1):
    base, exponent = ret
    exponential = exponent * log(base)
    if exponential > max_exponential:
      max_exponential = exponential
      max_i = i

  print(max_i)

# strategy:
# - since log grows monotonically you can say:
#   a^b > c^d   if   log(a^b) > log(c^d)  == b*log(a) > d*log(c)
