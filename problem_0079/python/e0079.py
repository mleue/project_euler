def read_keys():
  """Return list of keys read from the file."""
  keys = []
  with open('keylog.txt') as f:
    for line in f:
      keys.append(list(line.strip()))
  return keys


def apply_sort(charset, key):
  """Sort the charset according to the char order in each key."""
  combinations = [(key[0], key[1]), (key[0], key[2]), (key[1], key[2])]

  # TODO the operations here are super inefficient for a list
  # but it might be okay given the low n of the task?
  for before, after in combinations:
    i_before, i_after = charset.index(before), charset.index(after)
    if i_before > i_after:
      charset.insert(i_before+1, charset[i_after])
      del charset[i_after]


if __name__ == '__main__':
  keys = read_keys()
  charset = list(set([char for key in keys for char in key]))
  print(charset)
  for key in keys:
    apply_sort(charset, key)
  print(charset)
