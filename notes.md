#Some notes and findings while solving these problems
##General
* read the question carefully and don't compute/store any data that is not being asked for
  * e.g. don't compute all prime numbers when only the largest prime factor is asked for
  * e.g. don't store all elements if only their sum is asked for 
* the algorithm should run in under a minute on a regular computer

##Mathematics
* fibonacci numbers are created by continuously adding the previous and current number, starting with (1,2)
* eratosthenes sieve is a simple method for finding all prime numbers below a certain threshold
 * works by iterating through all smaller prime numbers and removing all their multiples from the potential pool of integers
* every non-prime number can be factorized using only prime numbers

##CPP
* in a recursive approach where each recursion also loops over some variable, don't forget to break the loop if you invoke a recursion from inside the loop
