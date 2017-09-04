from itertools import permutations


def print_magic_5_gon_solution():
  """Yield potential solutions for the magic 5 gon."""
  # we want the outer digits to be the high ones to get a high final number
  outer_perms = list(permutations([6, 7, 8, 9, 10]))
  inner_perms = list(permutations([1, 2, 3, 4, 5]))

  # outer nodes are called a,b,c,d,e
  for a, b, c, d, e in outer_perms:
    # according to the problem description the lowest outer node
    # will be the first digit of the number, so we can disregard
    # all that are not 6
    if a != 6:
      continue
    # inner nodes are called f,g,h,i,j
    for f, g, h, i, j in inner_perms:
      if a+f+g == b+g+h == c+h+i == d+i+j == e+j+f:
        print("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
              .format(a, f, g, b, g, h, c, h, i, d, i, j, e, j, f))


if __name__ == '__main__':
  print_magic_5_gon_solution()
