coins = (200, 100, 50, 20, 10, 5, 2, 1)

def possibilities(target, maxcoin):
  count = 0
  #if we can fill up with 1p coins, we can always add 1
  if maxcoin == 7:
    return 1
  for i in range(maxcoin, 8):
    rest = target - coins[i]
    if rest == 0:
      count += 1
    elif rest > 0:
      count += possibilities(rest, i)
  return count

print(possibilities(200, 0))
