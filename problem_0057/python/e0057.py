def sqrt2_expansion(n):
  """advance the sqrt(2) expansion"""
  num, denum = 3, 2
  add_num, add_denum = 4, 3
  yield (num, denum)
  for _ in range(n-1):
    num, denum = num+add_num, denum+add_denum
    yield (num, denum)
    prev_add_denum = add_denum
    add_denum = add_num + add_denum
    add_num = prev_add_denum + add_denum

if __name__ == '__main__':
  count = 0
  for num, denum in sqrt2_expansion(1000):
    if len(str(num)) > len(str(denum)):
      count += 1

  print(count)
