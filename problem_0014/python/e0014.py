def collatz_sequence_length(start, lookup):
  """return collatz sequence length starting on start"""
  curr = start
  count = 1
  while curr > 1:
    if curr in lookup:
      lookup[start] = lookup[curr] + count - 1
      return None
    elif curr % 2 == 0:
      curr //= 2
    else:
      curr = curr*3 + 1
    count += 1

  lookup[start] = count

def longest_collatz_sequence_below_n(n):
  """return longest collatz sequence that starts below n"""
  lookup = dict()
  for i in range(n):
    if i % 100000 == 0:
      print(i)
    collatz_sequence_length(i, lookup)

  max_key, max_value = max(lookup.items(), key=(lambda kv: kv[1]))
  return max_key, max_value

if __name__ == '__main__':
  n = 1000000
  print("The longest collatz sequence starting from below {} has seed {} and length {}."
        .format(n, *longest_collatz_sequence_below_n(1000000)))
