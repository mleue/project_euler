def fib():
  """an infinite fibonacci generator"""
  a, b = 1, 0
  while True:
    yield a
    a, b = a+b, a

if __name__ == '__main__':
  l = 1000
  fibonacci = fib()
  count = 1
  while len(str(next(fibonacci))) < l:
    count += 1
  print("The {}th is the first fibonacci number with at least {} digits."
        .format(count, l))
