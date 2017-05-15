import re

def char_score(c):
  """return alphabetic score of the char c, e.g. 3 for 'C' and 26 for 'Z'"""
  return ord(c.upper()) - ord('A') + 1

def read_names_file(filename):
  """return list of all names in the names file"""
  with open(filename, mode='r', encoding='utf-8') as f:
    names = re.findall(r'"([^"]+)"', f.read())
  return names

def compute_total_name_score(filename):
  """return the total name score for all names in the names file"""
  names = read_names_file(filename)
  names_sorted = sorted(names)
  total_score = 0
  for pos, name in enumerate(names_sorted, 1):
    name_score = sum((char_score(c) for c in name))
    total_score += pos*name_score

  return total_score

if __name__ == '__main__':
  filename = 'names.txt'
  print("The total score for all names in {} is {}"
        .format(filename, compute_total_name_score(filename)))
