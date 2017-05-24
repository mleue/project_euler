def is_curious_fraction(num_str, den_str):
  """check if num_str/den_str is a curious fraction"""
  common_elements = set(num_str).intersection(den_str)

  if len(common_elements) != 1:
    return False

  to_cancel = list(common_elements)[0]
  if to_cancel == '0':
    return False
    
  num_canceled = ''.join([d for d in num_str if d != to_cancel])
  den_canceled = ''.join([d for d in den_str if d != to_cancel])

  if len(num_canceled) == 0 or len(den_canceled) == 0 or den_canceled == '0':
    return False

  if int(num_canceled)/int(den_canceled) == int(num_str)/int(den_str):
    return True
  else:
    return False

if __name__ == '__main__':
  curious_fractions = []
  num, den = 1, 1
  for i in range(10, 100):
    for j in range(i+1, 100):
      if is_curious_fraction(str(i), str(j)):
        curious_fractions.append((i, j))
        num *= i
        den *= j
  print(curious_fractions)
  print(num)
  print(den)
