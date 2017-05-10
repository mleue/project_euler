def factorial(n):
  """return n!"""
  if not n > 1:
    return n or 1
  else:
    return n * factorial(n - 1)

def lattice_path_permutations(dim):
  """return the number of lattice paths that can be taken in a dimXdim grid

  this is a permutation problem:
  - we are only allowed to go 'r' or 'd'
  - we know we have to go dim*'r' and dim*'d' to reach the goal
  -> we need to find the unique permutations of the string dim*'r' + dim*'d'
  - why unique permutations?
  -> because e.g. in a 2X2 grid you can reach the goal via
   * 'rrdd' [0123], but also via 'rrdd' [1023] -> the 'r's and 'd's are interchangeable"""

  #factorial(dim*2) gives us **all** permutations of 'rrr...ddd' (including non-unique)
  #we have to divide this number by the number of ways in which both the 'r's and the 'd's
  #in those permutations can be permuted which is factorial(dim) for each of them
  return factorial(dim*2) // factorial(dim)**2

  #this could be sped up by cancelling the factorial computation
  #e.g. for a 2x2 grid (1*2*3*4)/((1*2)*(1*2)) = (3*4)/(1*2)
  #but that would involve a bit more code

if __name__ == '__main__':
  dim = 20
  print("The number of lattice paths through a {}X{} grid is {}"
        .format(dim, dim, lattice_path_permutations(dim)))
