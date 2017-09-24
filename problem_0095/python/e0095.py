from math import sqrt, floor


def is_divisible_by(n, x):
  """Return True if n is divisible by x, False if not."""
  return n % x == 0


def divisor_sums(thresh):
  """Return dict of divisor sums for all even numbers < thresh."""
  div_sums = {}
  for i in range(2, thresh, 2):
    if not is_divisible_by(i, 2):
      continue
    divisors = [1]
    for j in range(2, floor(sqrt(i))):
      if is_divisible_by(i, j):
        divisors.append(i//j)
        divisors.append(j)
    div_sums[i] = sum(divisors)

  return div_sums


def get_longest_amicable_chain(div_sums):
  """Return first element of longest amicable chain of divisor sums."""
  longest_count, longest_start = 0, None
  for start in div_sums.keys():
    if not div_sums[start] > start:
      continue
    chain, el = set(), start
    while True:
      chain.add(el)
      el = div_sums[el]
      if el == start:
        if len(chain) > longest_count:
          longest_count, longest_start = len(chain), start
          break
      elif el not in div_sums or el in chain:
        break

  return longest_count, longest_start


# TODO faster
if __name__ == '__main__':
  threshold = 1000000
  div_sums = divisor_sums(threshold)
  assert div_sums[220] == 284
  assert div_sums[284] == 220
  print(get_longest_amicable_chain(div_sums))

# strategy:
# - create divisor sums for all n below thresholds (making use of that smaller
#   factor of clean division of n is max sqrt(n) )
# - relevant are only even numbers, because only they have divisor sums large
#   enough to actually potentially create a chain
# - for all divisor sums found, check if they build a chain and find the longest
