def factorial(n):
  """return n!"""
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

def n_combinations(n, r, factorials):
  """return number of combinations from n and r"""
  return factorials[n] // (factorials[r] * factorials[n-r])

if __name__ == '__main__':
  thresh = 1000000
  factorials = {n: factorial(n) for n in range(101)}
  count = 0
  for n in range(101):
    for r in range(n + 1):
      if n_combinations(n, r, factorials) > thresh:
        count += 1

  print(count)
