from math import sqrt
from itertools import permutations


def generate_cuboids():
  """Continously yield unique integer cuboids in increasing size order."""
  yield (1, 1, 1)
  c = 2
  while True:
    for a in range(1, c+1):
      for b in range(a, c+1):
        yield (a, b, c)
    c += 1


def shortest_path_is_integer(a, b, c):
  """Return True if cuboid a, b, c has a shortest integer path to the opposite corner."""
  # route_permutations = list(permutations((a, b, c)))[::2]

  # shortest_route = None
  # for x, y, z in route_permutations:
  #   route_length = x**2 + (y+z)**2
  #   if shortest_route is None:
  #     shortest_route = route_length
  #   else:
  #     if shortest_route > route_length:
  #       shortest_route = route_length

  # return sqrt(shortest_route).is_integer()
  return sqrt(c**2 + (a+b)**2).is_integer()


def calc_square_set(c):
  square_set = set()
  c_square = c**2
  for ab in range(2, 2*c):
    if sqrt(c_square + ab**2).is_integer():
      square_set.add(ab)
  return square_set


if __name__ == '__main__':
  cuboids = generate_cuboids()
  shortest_path_is_integer_count = 0
  latest_c, square_set = 1, set()
  # while True:
  #   a, b, c = next(cuboids)
  #   if latest_c != c:
  #     latest_c = c
  #     square_set = calc_square_set(c)
  #   # if shortest_path_is_integer(a, b, c):
  #   if a+b in square_set:
  #     shortest_path_is_integer_count += 1
  #     if shortest_path_is_integer_count % 1000 == 0:
  #       print(shortest_path_is_integer_count, c)

  # TODO optimize
  overall_count = 0
  while True:
    square_set = calc_square_set(latest_c)
    count = 0
    for ab in square_set:
      if ab % 2 == 0:
        lower, upper = ab//2, ab//2
      else:
        lower, upper = ab//2, ab//2+1
      while upper <= latest_c and lower > 0:
        count += 1
        lower, upper = lower-1, upper+1
    overall_count += count
    # print("c: {}, count: {}, overall_count: {}".format(latest_c, count, overall_count))
    latest_c += 1
    if overall_count >= 1000000:
      print(latest_c)
      break

# strategy:
#   - the shortest way to the opposite corner is for the spider to cross
#     over any combination of two adjacent surfaces
#   - so there are 3 candidates for a shortest solution because in a cuboid
#     there are always at most 3 different surfaces
#   - the length of the shortest can be easily seen by "folding" one of the
#     surfaces over, which results in easily seeing that the direct path is
#     the hypotenuse of the right triangle with legs:
#       (a, b+c), (b, a+c), (c, a+b)
#       with a, b, c being the side lengths of the cuboid
#
#   - final strategy was actually to notice that the route where the longest
#     cuboid side is the lone, i.e. (longest, shorter+shorter) will result
#     in the shortest sqrt(longest**2, (shorter+shorter)**2) route
#   - so for every longest integer c we just have to first calculate all
#     values ab = shortest+shortest such that ab**2 + c**2 is a square, and thus
#     the sqrt(ab**2 + c**2) an integer
#   - then for all these values ab for each c we have to find the combinations
#     of integers that sum up to ab and are >0 and <=c, to do that we simply
#     divide ab//2 and then move up and down by 1 for every step and take a
#     count
