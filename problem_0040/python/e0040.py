if __name__ == '__main__':
  indices = {10**i for i in range(1, 7)}
  curr_number = 1
  curr_index = 1
  product = 1
  while indices:
    curr_number += 1
    curr_number_str = str(curr_number)
    curr_number_len = len(curr_number_str)
    for i in range(curr_number_len):
      index_to_check = curr_index + i + 1
      if index_to_check in indices:
        product *= int(curr_number_str[i])
        indices.remove(index_to_check)
        break
    curr_index += curr_number_len

  print("The product of the digits with the relevant indices is {} ."
        .format(product))
