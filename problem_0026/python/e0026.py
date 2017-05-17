from collections import defaultdict

def reciprocal_cycles(thresh):
  """return n below thresh for which 1/n has the longest recurring fractional part"""
  max_cycle_length = 0
  max_cycle_n = 0

  for n in range(2, thresh):
    #here we will store at what position we have seen a particular remainder
    remainder_to_fractional_position = defaultdict(int)
    #since all our fractions are 1/n, we always start with a remainder of 1
    current_remainder = 1
    #the fractional position we are looking at right now, i.e. .0123456789...
    pos = 0

    #while we both:
    # - encounter a remainder that we have not seen before (i.e. not assigned a position before)
    # - have a non-zero remainder
    while remainder_to_fractional_position[current_remainder] == 0 and current_remainder != 0:
      #perform division as on paper
      remainder_to_fractional_position[current_remainder] = pos
      current_remainder = (current_remainder * 10) % n
      pos += 1

    #cycle length as the distance between first seeing a particular remainder and then seeing it again
    #e.g. remainders for 1/7
    # 1 3 2 6 4 5 1
    # <----------->
    curr_cycle_length = pos - remainder_to_fractional_position[current_remainder]
    if curr_cycle_length > max_cycle_length:
      max_cycle_length = curr_cycle_length
      max_cycle_n = n 

  return max_cycle_n


if __name__ == '__main__':
  print(reciprocal_cycles(1000))

# the algo is quite intricate but is actually just based on how you would divide a number on paper
# e.g. 1/7:
#
# remainders:      1 3 2 6 4 5 1 3 ...
# divisor:         7 7 7 7 7 7 7 7 ...
# integer div:  0. 1 4 2 8 5 7 1 4 ...
#
# for every remainder you have to imagine multiplying it by 10 and then finding out the integer div result
# and putting the new remainder on top in the next column
#
# as you can see: the important part for spotting a recurring cycle is to observe the remainders,
# once we encounter a remainder that we have seen before, we know that we are in a loop that will
# repeat itself
# so at that point we can abort and know that the cycle length is the current position of the fraction
# minus the position where we first encountered that particular remainder
# the other case for aborting is when we actually reach a remainder of 0, because then we have divided
# succesfully and there is nothing more left to divide
