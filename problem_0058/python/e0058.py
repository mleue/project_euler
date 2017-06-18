def is_prime(n):
  """return True if n is prime"""
  if n % 2 == 0:
    return False
  if n % 3 == 0:
    return False

  i = 5
  w = 2
  while i * i <= n:
    if n % i == 0:
      return False
    i += w
    w = 6 - w
  return True

def generate_spiral_corners():
  """generator for spiral corners"""
  curr_corners = [1]
  curr_l = 3
  yield curr_l, curr_corners
  while True:
    curr_corner = curr_corners[-1]
    curr_corners = []
    for _ in range(4):
      curr_corner += curr_l - 1
      curr_corners.append(curr_corner)

    yield curr_l, curr_corners
    curr_l += 2

def l_for_ratio_below_10p():
  """return l where ratio of prime corners to corners first falls below 0.1"""
  num, den = 0, 0
  for l, corners in generate_spiral_corners():
    num += len([corner for corner in corners if is_prime(corner)])
    den += len(corners)
    print(l, num/den)
    if num/den < 0.1:
      return l

if __name__ == '__main__':
  print(l_for_ratio_below_10p())
