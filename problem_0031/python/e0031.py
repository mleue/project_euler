import math

target = 2.0
values = (2.0, 1.0, 0.5, 0.2, 0.1, 0.05, 0.02)
all_values = [[i*val for i in range(0, int(target/val) + 1)] for val in values]
two_pound_values, one_pound_values, fifty_p_values, twenty_p_values, ten_p_values, five_p_values, two_p_values = all_values

count = 0
for two_pounds in two_pound_values:
  curr_sum = two_pounds
  if curr_sum == target:
    count += 1
    break;
  elif curr_sum > target:
    break
  for one_pound in one_pound_values:
    curr_sum = two_pounds + one_pound
    if curr_sum == target:
      count += 1
      break;
    elif curr_sum > target:
      break
    for fifty_p in fifty_p_values:
      curr_sum = two_pounds + one_pound + fifty_p
      if curr_sum == target:
        count += 1
        break;
      elif curr_sum > target:
        break
      for twenty_p in twenty_p_values:
        curr_sum = two_pounds + one_pound + fifty_p + twenty_p
        if curr_sum == target:
          count += 1
          break;
        elif curr_sum > target:
          break
        for ten_p in ten_p_values:
          curr_sum = two_pounds + one_pound + fifty_p + twenty_p + ten_p
          if curr_sum == target:
            count += 1
            break;
          elif curr_sum > target:
            break
          for five_p in five_p_values:
            curr_sum = two_pounds + one_pound + fifty_p + twenty_p + ten_p + five_p
            if curr_sum == target:
              count += 1
              break;
            elif curr_sum > target:
              break
            for two_p in two_p_values:
              curr_sum = two_pounds + one_pound + fifty_p + twenty_p + ten_p + five_p + two_p
              if curr_sum == target:
                count += 1
                break;
              elif curr_sum > target:
                break
              else:
                count += 1

print(count)
