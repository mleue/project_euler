from math import sqrt
from primes import prime_sieve

primes = prime_sieve(50000)
primes_set = set(primes)


def combine_factor_sums(fs1, fs2):
  return (fs1[0] + fs2[0], fs1[1] + fs2[1])


if __name__ == '__main__':
  # for every product this will store a list of the sums that can be summed up
  # from all possible factorizations of that product along with the amount of
  # numbers that takes, so each entry in the list for every product will be a
  # tuple (sum, no_of_numbers)
  factor_sums_lookup = dict()

  # if we e.g. have a product sum entry 16: (8, 2) we know that one
  # factorization of the product 16 can be formed by 2 factors that sum up to 8
  # involving 2 numbers (4*4), in order to get a valid product-sum number the
  # sum would also have to be 16, so 16-8 1s (in order not to change the
  # product) would have to be added on to it, thus resulting in 2+8 = 10 numbers
  # involved, so for k=10 we could add 16 as the product-sum number in the
  # following dict
  product_sums = dict()

  # we need to calculate more products here than the ks we are interested in in
  # order to actually fill up all the ks up to our desired threshold
  for n in range(2, 30000):
    factor_sums_lookup[n] = set([(n, 1)])
    if n in primes_set:
      continue
    else:
      pfs_set = set()
      for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
          pfs_set.add(i)
      for f1 in pfs_set:
        f2 = n//f1
        for factor_sum_1 in factor_sums_lookup[f1]:
          for factor_sum_2 in factor_sums_lookup[f2]:
            combined_factor_sum = combine_factor_sums(factor_sum_1, factor_sum_2)
            factor_sums_lookup[n].add(combined_factor_sum)

    for factor_sum in factor_sums_lookup[n]:
      if factor_sum[1] > 1:
        k = n - factor_sum[0] + factor_sum[1]
        if k not in product_sums:
          product_sums[k] = n

  sum_list = [s for k, s in product_sums.items() if k <= 12000]
  # check that we really have 11999 entries
  print(len(sum_list))
  # use only unique values
  unique_sums = set(sum_list)
  print(sum(unique_sums))
