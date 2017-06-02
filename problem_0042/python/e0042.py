import re

def letter_value(letter):
  """return alphabetic value of an uppercase letter, e.g. 'C' -> 3"""
  return ord(letter) - ord('A') + 1

def word_value(word):
  """return alphabetic word value of a word, e.g. 'SKY' -> 19 + 11 + 25 = 55"""
  return sum((letter_value(letter) for letter in word.upper()))

def read_words_file(filename):
  """return the list of words in the file"""
  with open(filename) as words_file:
    return re.findall(r'"([^"]+)"', words_file.read())

def triangle_numbers_below_thresh(thresh):
  """return set of triangle numbers below the thresh"""
  triangle_set = set()
  n = 1

  while True:
    curr = int((1 / 2) * n * (n + 1))
    if curr > thresh:
      break
    triangle_set.add(curr)
    n += 1

  return triangle_set

if __name__ == '__main__':
  filename = 'words.txt'
  word_values_list = [word_value(word) for word in read_words_file(filename)]
  max_word_value = max(word_values_list)
  triangle_set = triangle_numbers_below_thresh(max_word_value)
  number_word_values_triangle = sum((1 if word_value in triangle_set else 0 
                                     for word_value in word_values_list))
  print("The number of words from {} whose word value is a triangle number is {}"
        .format(filename, number_word_values_triangle))
