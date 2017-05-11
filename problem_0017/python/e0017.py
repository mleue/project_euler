import re
import n2w

def truncate_number_word_output(number_to_words_func):
  """removes trailing '-' or ' and ' from number_to_words return"""
  def truncator(number):
    return re.sub('(-$|\sand\s$)', '', number_to_words_func(number))

  return truncator

@truncate_number_word_output
def number_to_words(number):
  """return natural language representation of a number"""
  number_string = str(number)
  if len(number_string) == 1:
    return n2w.single_digit[int(number_string)]
  elif len(number_string) == 2 and number < 20:
    return n2w.teens[int(number_string)]
  elif len(number_string) == 2:
    return n2w.double_digit[int(number_string[0]+'0')] + '-' + number_to_words(int(number_string[1]))
  elif len(number_string) == 3:
    return n2w.single_digit[int(number_string[0])] + ' hundred and ' + number_to_words(int(number_string[1:]))
  elif len(number_string) == 4:
    return n2w.single_digit[int(number_string[0])] + ' thousand'
  else:
    return None

def number_letter_counts(numbers):
  """return the count of letters used to describe the given numbers in natural language"""
  return sum([len(re.sub(r'[^a-z]', '', number_to_words(number))) for number in numbers])

if __name__ == '__main__':
  n_min = 1
  n_max = 1000
  rang = range(n_min, n_max+1)
  print("The count of all letters to describe the numbers from {} to {} in natural language is {}"
        .format(n_min, n_max, number_letter_counts(rang)))
