def cross_product(ll1, ll2):
  """Return cross product between 2 lists of lists."""
  cp = []
  for l1 in ll1:
    for l2 in ll2:
      cp.append(tuple(sorted(l1+l2)))
  return cp


def slow_partitions(target):
  """A brute-force slow algorithm."""
  summands = {1: [(1,)]}
  for n in range(2, 21):
    current = []
    for s1 in range(1, (n//2)+1):
      s2 = n-s1
      current.append((s2, s1))
      current.extend(cross_product(summands[s1], summands[s2]))
    current = list(set(current))
    print(len(current))
    summands[n] = current
  print(summands[9])
  print(len(summands[9]))


def calc_sign_exponent(k):
  """Calculate the sign and exponent of the euler function."""
  # https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
  sign = 1 if k % 2 == 1 else -1
  exponent = k*(3*k + 1) // 2
  return sign, exponent



# https://en.wikipedia.org/wiki/Partition_(number_theory)
if __name__ == '__main__':
  k, exponent = 1, 0
  signs_exponents = []
  while exponent <= 100:
    sign, exponent = calc_sign_exponent(-k)
    signs_exponents.append((sign, exponent))
    sign, exponent = calc_sign_exponent(k)
    signs_exponents.append((sign, exponent))
    k += 1
  # print(signs_exponents)

  p = {0: 1}
  target = 100
  for n in range(1, target+1):
    partition_sum = 0
    for sign, k in signs_exponents:
      if n-k > -1 and n-k in p:
        partition_sum += sign*p[n-k]
      else:
        p[n] = partition_sum
        break
  # print(p)

  print("The number of partitions of the number {} including itself are {}"
        .format(target, p[target]))
