def spiral_corner_generator(max_side_length):
  """return an iterator for yielding a succession of corners for a numerical spiral"""
  curr_value = 1
  yield curr_value
  corner_counter = 0
  curr_side_length = 3

  while curr_side_length <= max_side_length:
    curr_value += (curr_side_length - 1)
    corner_counter += 1

    #when we have all four corners for this layer,
    #reset the counter and go to the next layer
    if corner_counter > 3:
      corner_counter = 0
      curr_side_length += 2

    yield curr_value

if __name__ == '__main__':
  max_side_length = 1001
  print("The sum of all corner pieces in a {}X{} side length numerical spiral is {}"
        .format(max_side_length, max_side_length, sum(spiral_corner_generator(max_side_length))))
