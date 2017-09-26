from sudoku import solve


def read_sudoku_strings(filename="sudoku_strings.txt"):
  """Return list of sudoku strings."""
  sudoku_strings = []
  i = -1
  with open(filename) as f:
    for line in f:
      if "Grid" in line:
        sudoku_strings.append("")
        i += 1
      else:
        sudoku_strings[i] = sudoku_strings[i] + line.strip()

  return sudoku_strings


if __name__ == '__main__':
  strings = read_sudoku_strings()
  strings = [string.replace('0', '.') for string in strings]
  top_left_sum = 0
  for n, string in enumerate(strings):
    solution = solve(string)
    top_left = (solution['A1'], solution['A2'], solution['A3'])
    top_left_sum += int(''.join(top_left))
    print("{} {} {}".format(*top_left))
    # print("solved puzzle {}".format(n))
    # print("")
  print(top_left_sum)
