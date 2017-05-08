from collections import OrderedDict

def import_grid_from_file(filename):
  """return grid as numbers line by line reading from provided filename"""
  grid = []
  with open(filename, mode='r', encoding='utf-8') as f:
    for line in f:
      grid.append([int(number) for number in line.rstrip().split()])

  return grid

def create_grid_matrix(grid):
  """return matrix mapping of pos tuples (x, y) to number value"""
  pos_number_matrix = OrderedDict()
  for i, row in enumerate(grid):
    for j, number in enumerate(row):
      pos_number_matrix[(i, j)] = number

  return pos_number_matrix

def build_list_adjacent_n(pos_number_matrix, n):
  """return list of all n adjacent positions to each position in the matrix 
     in right, down, diag1(southeast) and diag2(northeast) direction"""
  adjacents = []
  for x_pos, y_pos in pos_number_matrix.keys():
    right, down, diag1, diag2 = [(x_pos, y_pos)], [(x_pos, y_pos)], [(x_pos, y_pos)], [(x_pos, y_pos)]

    for pos_diff in range(1, n):
      right.append((x_pos + pos_diff, y_pos))
      down.append((x_pos, y_pos + pos_diff))
      diag1.append((x_pos + pos_diff, y_pos + pos_diff))
      diag2.append((x_pos + pos_diff, y_pos - pos_diff))

    adjacents.append(right)
    adjacents.append(down)
    adjacents.append(diag1)
    adjacents.append(diag2)

  return adjacents

def largest_product_adjacent_n(adjacents, pos_number_matrix):
  """return the largest product of any of the lists of adjacent n numbers from the grid"""
  largest = 0
  for adjacent_n in adjacents:
    curr = 1
    for pos in adjacent_n:
      curr *= pos_number_matrix.get(pos, 0)
    largest = largest if largest > curr else curr
  return largest

if __name__ == '__main__':
  filename = 'grid.txt'
  n = 4
  pos_number_matrix = create_grid_matrix(import_grid_from_file(filename))
  adjacents = build_list_adjacent_n(pos_number_matrix, n)
  print("The largest product of {} adjacent numbers in the grid from {} is {}"
        .format(n, filename, largest_product_adjacent_n(adjacents, pos_number_matrix)))
