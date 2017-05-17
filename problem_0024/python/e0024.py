from itertools import permutations

if __name__ == '__main__':
  nth = 1000000
  pool = '0123456789'
  print("The {}th lexicographic permutation of {} is {}"
        .format(nth, pool, ''.join(list(permutations(pool))[nth-1])))
