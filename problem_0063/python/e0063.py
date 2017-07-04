if __name__ == '__main__':
  count = 0
  for i in range(1, 10):
    exponent = 1
    while len(str(i**exponent)) >= exponent:
      if len(str(i**exponent)) == exponent:
        count += 1
      exponent += 1

  print(count)
