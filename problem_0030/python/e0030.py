#9^5 ~ 60k, so for every additional the max number that can be reached grows by 60k
#->it is sufficient to check until ~400k
powers_sum = 0
powers_lookup = {str(n): n**5 for n in range(10)}
for n in range(2, 400000):
  if sum((powers_lookup[digit] for digit in str(n))) == n:
    powers_sum += n

print(powers_sum)
