def read_numbers_file(filename):
  """return 2d list of digits that make up the numbers (each row is one number)"""
  digits_list_2d = []
  with open(filename, mode='r', encoding='utf-8') as f:
    for number_string in f:
      digits_list_2d.append([int(digit) for digit in number_string.rstrip()])

  return digits_list_2d

def carry_over_reduce(number_list):
  """performs a reduce on a list to carry the sum carry and reduce all numbers to single digits"""
  #e.g. [12, 15, 18] -> [12, 16, 8] -> [13, 6, 8] -> [1, 3, 6, 8] -> [1, 3, 6, 8]
  carry = 0
  reduced_list = []
  for number in number_list[::-1]:
    number_string = str(number + carry)
    reduced_list.append(int(number_string[-1]))

    if len(number_string) > 1:
      carry = int(number_string[:-1])
    else:
      carry = 0

  if carry > 0:
    reduced_list.extend([int(digit) for digit in str(carry)])

  return reduced_list[::-1]

def transpose_2d_list(list_2d):
  """return transposed 2d list"""
  return list(zip(*list_2d))

def written_sum(list_2d):
  """return the sum of a 2d-list of rows of digit lists"""
  written_summation_individual_sums = [sum(digits) for digits in transpose_2d_list(list_2d)]
  return carry_over_reduce(written_summation_individual_sums)

if __name__ == '__main__':
  filename = 'numbers.txt'
  n = 10
  print("The first {} digits of the sum of all numbers in {} is {}"
      .format(n, filename, written_sum(read_numbers_file(filename))[:n]))
