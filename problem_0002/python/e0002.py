def fibonacci(max_thresh):
  """return fibonacci numbers below the max threshold"""
  a, b = 1, 1
  while a < max_thresh:
    yield a
    a, b = b, a+b

def solution(max_thresh):
  """returns the sum of all even fibonacci numbers below the max threshold"""
  return sum([n for n in fibonacci(max_thresh) if n % 2 == 0])

if __name__ == '__main__':
  max_thresh = 4000000
  print("The sum of all even fibonacci numbers below {} is {}"
        .format(max_thresh, solution(max_thresh)))
