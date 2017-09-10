def factorial(n):
  """Return n! ."""
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)


def factorial_digit_sum(n, factorials):
  """Return sum of factorials of digits of n, e.g. 169 -> 363601."""
  return sum(factorials[d] for d in str(n))


# TODO can probably be sped up by keeping a dict of already solved
# factorial_digit_sums and thus not recalculating anything we've seen before
def factorial_chain_length(n, factorials, thresh=60):
  """Return factorial chain length for n if < thresh, thresh + 1 otherwise."""
  chain = set([n])
  while True:
    n = factorial_digit_sum(n, factorials)
    if n in chain:
      return len(chain)
    else:
      chain.add(n)
      if len(chain) > thresh:
        return thresh + 1


if __name__ == '__main__':
  factorials = {str(n): factorial(n) for n in range(10)}
  limit, threshold, amount = 1000000, 60, 0
  for number in range(limit):
    if number % 100000 == 0:
      print(number)
    if factorial_chain_length(number, factorials, threshold) == threshold:
      amount += 1
  print(amount)

# strategy:
# - precalculating the factorials for each digit 0-9
# - to determine the chain length for each n we keep a set of terms that have
#   occured and as soon as a term appears that is already in the set we return
#   the length of the set
