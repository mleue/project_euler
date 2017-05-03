def multiples_of_x_below_y(x, y):
  """return list of multiples of x smaller than y"""
  multiples = []
  z = x
  while z < y:
    multiples.append(z)
    z += x

  return multiples

def solution(number_list, threshold):
  """return the sum of all multiples of numbers in number_list below threshold"""
  multiples = []
  for number in number_list:
    multiples += multiples_of_x_below_y(number, threshold)

  #there may be duplicates, we only want unique values
  unique_multiples = set(multiples)

  return sum(unique_multiples)

if __name__ == '__main__':
  number_list = [3, 5]
  threshold = 1000
  print("The sum of all multiples of {} below {} is {}"
        .format(number_list, threshold, solution(number_list, threshold))) 
