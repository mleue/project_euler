def diff_to_x(n, x):
  """Return diff of n to x."""
  return abs(n - x)


if __name__ == '__main__':
  target = 2000000
  min_diff, min_pos = target, (0, 0)
  for x in range(200):
    for y in range(200):
      val = (x*(x+1)//2) * (y*(y+1)//2)
      if diff_to_x(val, target) < min_diff:
        min_diff, min_pos = diff_to_x(val, target), (x, y)

  print(min_diff, min_pos, min_pos[0]*min_pos[1])

# strategy:
# - sum in x direction: x(1+x)/2
# - sum in y direction: y(1+y)/2
# - overall sumX*sumY
