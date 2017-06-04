def generate_pentagonal_numbers_below_thresh(thresh):
  """return list of pentagonal numbers below the threshold"""
  n = 1
  while True:
    curr = (n*(3*n - 1)) // 2
    if curr > thresh:
      break
    else:
      yield curr
      n += 1

if __name__ == '__main__':
  thresh = 10000000
  pentagonals = list(generate_pentagonal_numbers_below_thresh(thresh))
  pentagonal_set = set(pentagonals)
  for i, n1 in enumerate(pentagonals):
    for n2 in pentagonals[i+1:]:
      if n1 + n2 in pentagonal_set and n2 - n1 in pentagonal_set:
        print(n2 - n1)
