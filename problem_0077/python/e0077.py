from collections import defaultdict
from primes import prime_sieve

primes = prime_sieve(1000)


# TODO refactor
def prime_partitions(target_partitions):
  """Return the first n for which the target prime partitions can be created."""
  n = 2
  while True:
    partitions = defaultdict(int)
    partitions[0] = 1
    i = 0
    while primes[i] < n:
      for j in range(primes[i], n+1):
        partitions[j] = partitions[j] + partitions[j-primes[i]]
      i += 1

    print(n, partitions[n])
    if partitions[n] > target_partitions:
      break
    n += 1

  return n


if __name__ == '__main__':
  print(prime_partitions(target_partitions=5000))
