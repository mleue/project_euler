import math

def is_int(float_number):
  """return True if the float could be represented as an int, False otherwise"""
  return math.floor(float_number) == float_number

def quadratic_solution(a, b, c):
  """return the pos solution to the standard quadratic equation ax^2 + bx + c = 0"""
  return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

def is_triangle_number(number):
  """return if number is a triangle number
     based on checking if the solution of the quadratic equation is an int"""
  a, b, c = 1, 1, -2*number
  pos_x = quadratic_solution(a, b, c)
  return is_int(pos_x)

def is_pentagonal_number(number):
  """return if number is a pentagonal number
     based on checking if the solution of the quadratic equation is an int"""
  a, b, c = 3, -1, -2*number
  pos_x = quadratic_solution(a, b, c)
  return is_int(pos_x)

def generate_hexagonals(start_n):
  """return infinite generator for hexagonals from start_n on"""
  n = start_n
  while True:
    yield n*(2*n - 1)
    n += 1

if __name__ == '__main__':
  start_n = 144
  hex_gen = generate_hexagonals(start_n)
  while True:
    curr_hex = next(hex_gen)
    if is_pentagonal_number(curr_hex) and is_triangle_number(curr_hex):
      break
  print("The second number to be triangle, pentagonal and hexagonal is {}"
        .format(curr_hex))
