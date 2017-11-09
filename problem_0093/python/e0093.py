from itertools import permutations, product, combinations


def add_variables(equation, variables):
  """Add the a,b,c,d variables to the equation at the right spots."""
  for i, j in enumerate(range(2, 17, 4)):
    equation[j] = variables[i]


def add_operations(equation, operations):
  """Add the operations to the equation at the right spots."""
  for i, j in enumerate(range(3, 17, 5)):
    equation[j] = operations[i]


def add_brackets(equation, brackets):
  """Add the brackets to the equation at the right spots."""
  for pos, brace in brackets.items():
    equation[pos] = brace


def chain_length(seq):
  """Return chain length of sequence starting on one."""
  compare = 1
  for i in range(len(seq)):
    if not compare == seq[i]:
      return compare
    else:
      compare += 1
  return compare



# TODO make it faster
if __name__ == '__main__':
  bracket_variants = [
      {0: '(', 7: ')'},
      {4: '(', 11: ')'},
      {9: '(', 15: ')'},
      {0: '(', 12: ')'},
      {4: '(', 16: ')'},
      {0: '(', 1: '(', 7: ')', 11: ')'},
      {0: '(', 4: '(', 11: ')', 12: ')'},
      {4: '(', 5: '(', 11: ')', 15: ')'},
      {4: '(', 9: '(', 15: ')', 16: ')'},
  ]
  max_chain_length = 0
  for numbers in combinations([str(float(i)) for i in range(1, 10)], r=4):
    solutions = set()
    for variables in permutations(numbers):
      for operators in product(['*', "+", "/", "-"], repeat=4):
        for brackets in bracket_variants:
          equ = ['']*17
          add_variables(equ, variables)
          add_operations(equ, operators)
          add_brackets(equ, brackets)
          try:
            value = eval(''.join(equ))
            if value.is_integer():
              solutions.add(value)
          except ZeroDivisionError:
            pass
    output_chain = sorted([int(sol) for sol in solutions if int(sol) > 0])
    l = chain_length(output_chain)
    if l > max_chain_length:
      max_chain_length = l
      print(numbers)
      print(l)
      print(output_chain)
      print("")
