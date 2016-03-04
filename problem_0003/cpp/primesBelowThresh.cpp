#include <vector>
#include <iostream>
#include "number.h"

using namespace::std;

//TODO prettier way of advancing to the next prime Number, e.g. a checked? flag
int getNextPrime(long basePrime, vector<Number> &primes) {
	for(vector<Number>::iterator it = primes.begin() + basePrime + 1; it != primes.end(); ++it) {
		if (it->isPrime == true) {
			return it->value;
		}
	}
}

void erastothenes(long basePrime, vector<Number> &primes) {
	long thresh = primes.size();
	if (basePrime > ((thresh/2)+1))
		return;

	for (long i=2; i < ((thresh/basePrime)+1); ++i)
		primes[i*basePrime].isPrime = false;

	basePrime = getNextPrime(basePrime, primes);
	erastothenes(basePrime, primes);
}

//TODO use a class to store the number, the accompanying primes, and the largest prime factor
//TODO remove all those that are not primes to save memory
//TODO zero is not a prime number ;)
//TODO user input for number
int main() {
	//long number = 600851475143;
	//long number = 13195;
	long number = 105;
	vector<Number> primes;
	for (long i=0; i<=number; ++i) {
		primes.push_back(Number(i));
	}

	erastothenes(2, primes);

	cout << "All prime numbers smaller than " << number << " are:" << endl;

	for(vector<Number>::iterator it = primes.begin(); it != primes.end(); ++it) {
		if (it->isPrime)
			cout << it->value << endl;
	}
}
