def read_matrix(filename='matrix.txt'):
  """Return list of list of matrix entries."""
  matrix = []
  with open(filename) as f:
    for line in f:
      row = line.strip().split(',')
      row = [int(number_str) for number_str in row]
      matrix.append(row)
  return matrix


def update_value(x, y, x_prev, y_prev, matrix_dict):
  """Update the value at x, y with to_add if necessary."""
  to_add = matrix_dict[(x_prev, y_prev)]['accumulated_value']
  if to_add is None:
    to_add = matrix_dict[(x_prev, y_prev)]['value']
  values_sum = matrix_dict[(x, y)]['value'] + to_add

  # if no accumulated value is present in the cell yet, update it
  if matrix_dict[(x, y)]['accumulated_value'] is None:
    matrix_dict[(x, y)]['accumulated_value'] = values_sum
    matrix_dict[(x, y)]['parent'] = (x_prev, y_prev)
    return True
  # else, update only if the new accumulated value would be lower
  else:
    if values_sum < matrix_dict[(x, y)]['accumulated_value']:
      matrix_dict[(x, y)]['accumulated_value'] = values_sum
      matrix_dict[(x, y)]['parent'] = (x_prev, y_prev)
      return True
  return False


def is_valid_index(x, y, l_matrix):
  """Return True if x, y is a valid index, False if not."""
  return x < l_matrix and y < l_matrix and x > -1 and y > -1


def roll_up_matrix(matrix_dict, l_matrix):
  """Roll up the matrix dict.

  Every cell's value must be it's own value plus the minimum additions of any
  of the cells it can be reached from.
  """
  frontier = set([(x, 0) for x in range(l_matrix)])
  while frontier:
    new_frontier = set()
    for x, y in frontier:
      # down
      if is_valid_index(x+1, y, l_matrix):
        updated = update_value(x+1, y, x, y, matrix_dict)
        if updated:
          new_frontier.add((x+1, y))
      # right
      if is_valid_index(x, y+1, l_matrix):
        updated = update_value(x, y+1, x, y, matrix_dict)
        if updated:
          new_frontier.add((x, y+1))
      # up
      if is_valid_index(x-1, y, l_matrix):
        updated = update_value(x-1, y, x, y, matrix_dict)
        if updated:
          new_frontier.add((x-1, y))
    frontier = new_frontier


def init_matrix_cell(value):
  """Return an initial matrix cell object."""
  return {
    'value': value,
    'accumulated_value': None,
    'parent': None
  }


if __name__ == '__main__':
  # read matrix as list of lists
  matrix = read_matrix()
  l_matrix = len(matrix[0])
  assert matrix[-1][-1] == 7981
  assert matrix[l_matrix-1][l_matrix-1] == 7981

  # convert to dict of pos -> cell
  matrix_dict = {(i, j): init_matrix_cell(matrix[i][j])
                 for i in range(len(matrix)) for j in range(len(matrix))}
  assert matrix_dict[(l_matrix-1, l_matrix-1)]['value'] == 7981

  # roll up
  roll_up_matrix(matrix_dict, l_matrix)
  right_column = [matrix_dict[(x, l_matrix-1)] for x in range(l_matrix)]
  print(right_column)
  print(min([cell['accumulated_value'] for cell in right_column]))

# differences to 0081:
#
# - if no accumulated value is present, use the value entry to add to the
# neighbour
# - an additional step in the roll-up (an up-step, i.e. x-1)
# - the initial frontier is the entire left column (i.e. all x for y=0)
# - only add cell to the new frontier if it's value was updated (otherwise we
# can find the same cell over and over again and go in a loop by going up-down)
