def distinct_combinations(a_max, b_max):
  """return all distinct combinations a^b for a = [2, a_max], b = [2, b_max]"""
  combinations = set()
  for a in range(2, a_max+1):
    for b in range(2, b_max+1):
      combinations.add(a**b)

  return len(combinations)

if __name__ == '__main__':
  n = 100
  print(distinct_combinations(n, n))
