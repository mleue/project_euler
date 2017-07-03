def triangle(n):
  return n*(n+1) // 2

def square(n):
  return n**2

def pentagonal(n):
  return n*(3*n-1) // 2

def hexagonal(n):
  return n*(2*n-1)

def heptagonal(n):
  return n*(5*n-3) // 2

def octagonal(n):
  return n*(3*n-2)

def generate_numbers(thresh, func):
  n, number = 1, 1
  while number < thresh:
    yield number
    n += 1
    number = func(n)

def cycle_through(curr_number, used_categories, used_numbers, first_2_to_num, num_to_cat):
  """build up a cyclic sequence recursively"""
  #once we have a sequence of 6 that connects the end to the beginning, we are done
  if len(used_numbers) == 6 and used_numbers[-1][-2:] == used_numbers[0][:2]:
    print(used_numbers)
    print([num_to_cat[number] for number in used_numbers])
    print(sum(int(number) for number in used_numbers))
    return
  last_2_digits = curr_number[-2:]
  if last_2_digits[0] == '0':
    return False
  cyclic_possibilities = first_2_to_num[last_2_digits]
  if cyclic_possibilities:
    for possible_num in cyclic_possibilities:
      if possible_num in used_numbers:
        continue
      possible_cat = num_to_cat[possible_num]
      for cat in possible_cat:
        if cat not in used_categories:
          categories = set(used_categories)
          categories.add(cat)
          numbers = list(used_numbers)
          numbers.append(possible_num)
          cycle_through(possible_num, categories, numbers, first_2_to_num, num_to_cat)


if __name__ == '__main__':
  #generate all numbers from all 6 functions and save them in a dict under the respective category
  functions = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
  category_to_numbers = {i: [str(number) for number in generate_numbers(10000, func) if number > 1000] for i, func in enumerate(functions)}
  all_numbers = [number for cat, nums in category_to_numbers.items() for number in nums]
  #print([(category, numbers) for category, numbers in category_to_numbers.items()])
  #print("{} numbers in total".format(len(all_numbers)))

  #map each number to a set of all categories that it appears in
  number_to_categories = dict()
  for category, numbers in category_to_numbers.items():
    for number in numbers:
      if number in number_to_categories:
        number_to_categories[number].add(category)
      else:
        number_to_categories[number] = {category}
  #print(number_to_categories)

  #map each initial 2 digits of a number to all numbers those may belong to
  number_first_2_digits_to_numbers = dict()
  for number in all_numbers:
    first_2 = number[:2]
    if first_2 in number_first_2_digits_to_numbers:
      number_first_2_digits_to_numbers[first_2].add(number)
    else:
      number_first_2_digits_to_numbers[first_2] = {number}
  #print(number_first_2_digits_to_numbers)

  #using each number in each category as the starting point, cycle through all possibilities according to the rule
  #and see if we can build a sequence of 6 numbers that fulfill the properties
  for category, numbers in category_to_numbers.items():
    for number in numbers:
      cycle_through(number, {category}, [number], number_first_2_digits_to_numbers, number_to_categories)
