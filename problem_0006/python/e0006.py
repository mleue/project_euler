import itertools
import time

def sum_square_diff_1(rang):
  """returns the diff between sum of squares and square of the sum"""
  #brute-force implementation
  return sum(rang)**2 - sum([x**2 for x in rang])

def sum_square_diff_2(rang):
  """returns the diff between sum of squares and square of the sum"""
  #somewhat smarter implementation based on breaking up the multinomial
  #and removing the square terms
  #https://en.wikipedia.org/wiki/Multinomial_theorem
  return sum([x*y for x, y in itertools.permutations(rang, 2)])

def timer_test(rang):
  """prints the timing results of both algos"""
  start = time.time()
  sum_square_diff_1(rang)
  time1, start = time.time()-start, time.time()
  sum_square_diff_2(rang)
  time2 = time.time()-start
  print("The time for each algo is {:.5f} and {:.5f}".format(time1, time2))

if __name__ == '__main__':
  lower = 1
  upper = 101
  rang = range(lower, upper)
  print("The diff of the sum of squares and the square of the sum in range({}, {}) is {}".format(lower, upper, sum_square_diff_1(rang)))
  timer_test(rang)
  timer_test(range(1, 1001))
