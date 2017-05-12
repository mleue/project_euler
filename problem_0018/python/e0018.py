def read_triangle(filename):
  """return 2d list of rowsXnumbers of the triangle to read"""
  with open(filename, mode='r', encoding='utf-8') as f:
    return [[int(n_str) for n_str in row.strip().split()] for row in f]

def add_lists_elementwise(list1, list2):
  """return [l1_1+l2_1, l1_2+l2_2, ...]"""
  return [sum(combination) for combination in zip(list1, list2)]

def reduce_list_consecutive_max_neighbors(number_list):
  """return e.g. [5, 8, 8] for input [4, 5, 8, 3]"""
  max_neighbor_list = []
  for i in range(len(number_list)-1):
    max_neighbor = number_list[i] if number_list[i] > number_list[i+1] else number_list[i+1]
    max_neighbor_list.append(max_neighbor)
  return max_neighbor_list

def roll_up_triangle(row_number_list):
  """roll up the triangle from the bottom"""
  #for each row, we check if there is a previous row to add on top
  #if yes, add it
  #then we reduce the current row to its consecutive max neighbors
  #and set this to be the list that will be added on top of the following row
  to_add = []
  for row in row_number_list[::-1]:
    if to_add:
      row = add_lists_elementwise(to_add, row)
    to_add = reduce_list_consecutive_max_neighbors(row)
  return row[0]
  
if __name__ == '__main__':
  triangle_file = 'numberTriangle.txt'
  triangle = read_triangle(triangle_file)
  print("The maximum total from top to bottom in the triangle in {} is {}"
        .format(triangle_file, roll_up_triangle(triangle)))

#e.g.
#      3                 3                   3              3+20
#    7   4       ->   7     4         -> 7+13  4+15    ->
#  2   4   6       2+8  4+9   6+9
#8   5   9   3
#
#-> max total in this triangle is 23
