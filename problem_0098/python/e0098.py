from itertools import permutations
from math import sqrt


def is_palindrome(word):
  """Return True if word is a palindrome."""
  return word == word[::-1]


def are_anagrams(word1, word2):
  """Return True if word is an anagram."""
  return sorted(word1) == sorted(word2)


def is_square(n):
  """Return True if number n is a square."""
  return sqrt(n).is_integer()


if __name__ == '__main__':
  assert is_palindrome('RACE') is False
  assert is_palindrome('ANNA') is True
  assert are_anagrams('RACE', 'CARE') is True

  with open("words.txt") as f:
    word_list = f.read().replace('"', '').split(',')

  anagram_pairs = []
  for i, word1 in enumerate(word_list):
    for j in range(i, len(word_list)):
      word2 = word_list[j]
      if word1 is not word2:
        if are_anagrams(word1, word2):
          if not is_palindrome(word1) and not is_palindrome(word2):
            anagram_pairs.append((word1, word2))
  print(anagram_pairs)

  for word1, word2 in anagram_pairs:
    print(word1, word2)
    # TODO speed up by only using numbers here that are squares when concatenated
    for numbers in permutations(range(10), len(word1)):
      if numbers[0] == 0:
        continue
      else:
        lookup = dict(zip(word1, [str(n) for n in numbers]))
        # fix this int/str conversion confusion
        if lookup[word2[0]] == '0':
          continue
        if is_square(int(''.join([lookup[char] for char in word1]))):
          if is_square(int(''.join([lookup[char] for char in word2]))):
            print(int(''.join([lookup[char] for char in word1])))
            print(int(''.join([lookup[char] for char in word2])))
