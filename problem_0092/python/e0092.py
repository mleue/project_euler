precomputed_digit_squares = {str(n): n**2 for n in range(10)}


def square_digit_sum(number):
  """Return the sum of the square of the digits of a number, e.g. 32 -> 13."""
  return sum(precomputed_digit_squares[digit] for digit in str(number))


# TODO speed up
if __name__ == '__main__':
  assert square_digit_sum(44) == 32

  threshold = 10000000
  chain_results = {89: 89, 1: 1}
  arrive_at_89 = 0
  for n in range(1, threshold):
    if n % 1000000 == 0:
      print(n, arrive_at_89)
    chain = []
    if n not in chain_results and n <= 567:
      while n not in chain_results:
        chain.append(n)
        n = square_digit_sum(n)
    else:
      n = square_digit_sum(n)
    for c in chain:
      chain_results[c] = chain_results[n]
    if chain_results[n] == 89:
      arrive_at_89 += 1

  print(arrive_at_89)
