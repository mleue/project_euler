if __name__ == '__main__':
  max_digit_sum = 0
  for a in range(100):
    for b in range(90, 100):
      digit_sum = sum(int(digit) for digit in str(a**b))
      if digit_sum > max_digit_sum:
        max_digit_sum = digit_sum

  print(max_digit_sum)
