def written_addition(summands):
  """Return written addition result of addition of the summands."""
  remainder, digits = 0, []
  for i in range(len(summands[0])-1, -1, -1):
    result = str(sum(int(summand[i]) for summand in summands) + remainder)
    if len(result) > 1:
      remainder = int(result[0])
      result = result[1]
    else:
      remainder = 0
    digits.append(result)

  return int(''.join(digits[::-1]))


def written_multiplication(n1, n2, last_n_digits=10):
  """Return the last_n_digits of the result of n1*n2."""
  n1, n2 = str(n1)[::-1], str(n2)[::-1]
  summands = []
  for i, digit1 in enumerate(n1[:last_n_digits]):
    if int(digit1) == 0:
      continue
    remainder, current = 0, i*['0']
    for digit2 in n2[:last_n_digits]:
      result = str(int(digit1) * int(digit2) + remainder)

      if len(result) > 1:
        remainder = int(result[0])
        result = result[1]
      else:
        remainder = 0

      current.append(result)
    current = current[:last_n_digits]
    summands.append(current[::-1])

  return written_addition(summands)


if __name__ == '__main__':
  a = 2**100000
  assert written_multiplication(1345, 6373, last_n_digits=3) == 685
  assert written_multiplication(1, a, last_n_digits=10) == int(str(a)[-10:])
  assert written_multiplication(28433, a, last_n_digits=10) == int(str(28433*a)[-10:])
  last_10_digits = 28433
  for j in range(78):
    last_10_digits = written_multiplication(last_10_digits, a)
  last_10_digits = written_multiplication(last_10_digits, 2**30457)
  last_10_digits += 1
  print(last_10_digits)


# strategy:
#   - you can split up the exponent of 2**7830457 into e.g.
#     (2**100000)**78 * 2**30457
#   - using written multiplication and addition you can calculate the last
#     n digits of these terms without having to perform the full operation
