target = 2.0
count = 0
for one_p in range(0, 201):
  one_p_sum = one_p*0.01
  if one_p_sum > target:
    break
  elif one_p_sum == target:
    count += 1
    break
  for two_p in range(0, 101):
    two_p_sum = one_p_sum + two_p*0.02
    if two_p_sum > target:
      break
    elif two_p_sum == target:
      count += 1
      break
    for five_p in range(0, 41):
      five_p_sum = two_p_sum + five_p*0.05
      if five_p_sum > target:
        break
      elif five_p_sum == target:
        count += 1
        break
      for ten_p in range(0, 21):
        ten_p_sum = five_p_sum + ten_p*0.10
        if ten_p_sum > target:
          break
        elif ten_p_sum == target:
          count += 1
          break
        for twenty_p in range(0, 11):
          twenty_p_sum = ten_p_sum + twenty_p*0.20
          if twenty_p_sum > target:
            break
          elif twenty_p_sum == target:
            count += 1
            break
          for fifty_p in range(0, 5):
            fifty_p_sum = twenty_p_sum + fifty_p*0.50
            if fifty_p_sum > target:
              break
            elif fifty_p_sum == target:
              count += 1
              break
            for one_pound in range(0, 3):
              one_pound_sum = fifty_p_sum + one_pound*1.00
              if one_pound_sum > target:
                break
              elif one_pound_sum == target:
                count += 1
                break
              for two_pounds in range(0, 1):
                two_pound_sum = one_pound_sum + two_pounds*2.00
                if two_pound_sum > target:
                  break
                elif two_pound_sum == target:
                  count += 1
                  break

print(count)
