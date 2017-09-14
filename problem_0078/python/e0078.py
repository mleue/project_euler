def calc_sign_exponent(k):
  """Calculate the sign and exponent of the euler function."""
  # https://en.wikipedia.org/wiki/Partition_(number_theory)#Generating_function
  sign = 1 if k % 2 == 1 else -1
  exponent = k*(3*k + 1) // 2
  return sign, exponent



# TODO: refactor
# https://en.wikipedia.org/wiki/Partition_(number_theory)
if __name__ == '__main__':
  k, exponent = 1, 0
  signs_exponents = []
  while exponent <= 100000:
    sign, exponent = calc_sign_exponent(-k)
    signs_exponents.append((sign, exponent))
    sign, exponent = calc_sign_exponent(k)
    signs_exponents.append((sign, exponent))
    k += 1
  # print(signs_exponents)

  print("starting to calc")
  p = {0: 1}
  target = 100000
  for n in range(1, target+1):
    if n % 1000 == 0:
      print(n)
    partition_sum = 0
    for sign, k in signs_exponents:
      if n-k > -1 and n-k in p:
        partition_sum += sign*p[n-k]
      else:
        p[n] = partition_sum
        if p[n] % 1000000 == 0:
          print(n)
  # print(p)

  print("The number of partitions of the number {} including itself are {}"
        .format(target, p[target]))
