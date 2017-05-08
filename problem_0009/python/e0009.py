import math

def c_fulfills_conditions(a, b, c, target_sum):
  """check whether c fulfills conditions of being an integer and a+b+c==target_sum"""
  return math.floor(c) == c and a + b + c == target_sum

def pythagorean_triplet(target_sum):
  """return the product abc of the pythagorean triplet that sums to target_sum"""
  #a can be at most sum//3 because of a+b+c==sum and a<b
  for a in range(target_sum//3, 1, -1):
    #b can be at most sum//2 because of a+b+c==sum and b<c
    for b in range(target_sum//2, a, -1):
      #calculate c for the current a and b
      c = math.sqrt(a**2 + b**2)
      if c_fulfills_conditions(a, b, c, target_sum):
        return a * b * math.floor(c)

if __name__ == '__main__':
  target_sum = 1000 
  print("The product abc of the three numbers fulfilling a<b, b<c and a+b+c=={} is {}"
        .format(target_sum, pythagorean_triplet(target_sum)))
