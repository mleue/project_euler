from copy import deepcopy


def fill_up_possibilities(possibilities):
  additional_possibilities = set()
  for A, B in possibilities:
    if len(A) < 6:
      for i in range(10):
        if i in A:
          continue
        new_A = deepcopy(A)
        new_B = deepcopy(B)
        new_A = set(new_A)
        new_A.add(i)
        new_A = frozenset(new_A)
        additional_possibilities.add(frozenset((frozenset(new_A), frozenset(new_B))))
    elif len(B) < 6:
      for i in range(10):
        if i in B:
          continue
        new_A = deepcopy(A)
        new_B = deepcopy(B)
        new_B = set(new_B)
        new_B.add(i)
        new_B = frozenset(new_B)
        additional_possibilities.add(frozenset((frozenset(new_A), frozenset(new_B))))
    else:
      additional_possibilities.add(frozenset((A, B)))
  return additional_possibilities


def deep_copy_sets(A, B):
  return deepcopy(A), deepcopy(B)


if __name__ == '__main__':
  pairs = [(0, 1), (0, 4), (0, 6), (1, 6), (2, 5),
           (3, 6), (4, 6), (6, 4), (8, 1)]
  possibilities = []
  for x, y in pairs:
    if not possibilities:
      possibilities = [({x, }, {y, }), ({y, }, {x, })]
    else:
      new_possibilities = []
      for A, B in possibilities:
        A_new_1, B_new_1 = deep_copy_sets(A, B)
        A_new_1.add(x)
        B_new_1.add(y)
        if not len(A_new_1) > 6 and not len(B_new_1) > 6:
          new_possibilities.append((A_new_1, B_new_1))
        A_new_2, B_new_2 = deep_copy_sets(A, B)
        A_new_2.add(y)
        B_new_2.add(x)
        if not len(A_new_2) > 6 and not len(B_new_2) > 6:
          new_possibilities.append((A_new_2, B_new_2))
      possibilities = new_possibilities

  print(len(possibilities))
  possibilities = set([frozenset((frozenset(A), frozenset(B))) for A, B in possibilities])
  print(len(possibilities))
  print([(len(A), len(B)) for A, B in possibilities])

  # add all sets where we can simply swap a 6 for a 9
  new_possibilities = set()
  for A, B in possibilities:
    if 6 in A:
      A_new, B_new = deep_copy_sets(A, B)
      A_new = set(A_new)
      A_new.remove(6)
      A_new.add(9)
      new_possibilities.add(frozenset((frozenset(A_new), frozenset(B_new))))
    if 6 in B:
      A_new, B_new = deep_copy_sets(A, B)
      B_new = set(B_new)
      B_new.remove(6)
      B_new.add(9)
      new_possibilities.add(frozenset((frozenset(A_new), frozenset(B_new))))
    if 6 in A and 6 in B:
      A_new, B_new = deep_copy_sets(A, B)
      A_new = set(A_new)
      A_new.remove(6)
      A_new.add(9)
      B_new = set(B_new)
      B_new.remove(6)
      B_new.add(9)
      new_possibilities.add(frozenset((frozenset(A_new), frozenset(B_new))))
  possibilities = possibilities.union(new_possibilities)
  print(len(possibilities))
  possibilities = fill_up_possibilities(possibilities)
  possibilities = fill_up_possibilities(possibilities)
  possibilities = fill_up_possibilities(possibilities)
  print([(len(A), len(B)) for A, B in possibilities])
  print(len(possibilities))
  # 1217
