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

//TODO don't use the index but rather the value the prime
void erastothenes(long basePrime, vector<Number> &primes) {
	long thresh = primes.size();
	if (basePrime > ((thresh/2)+1))
		return;

	for (long i=2; i < ((thresh/basePrime)+1); ++i)
		primes[i*basePrime].isPrime = false;

	basePrime = getNextPrime(basePrime, primes);
	erastothenes(basePrime, primes);
}

//TODO remove all those that are not primes to save memory
//TODO zero and one are no prime numbers ;)
int main() {
	long number = 1000000;
	long xth = 10001;
	vector<Number> primes;
	for (long i=0; i<=number; ++i) {
		primes.push_back(Number(i));
	}

	erastothenes(2, primes);

	cout << "The " << xth << "st prime number is: ";

	long i = 0;

	for(vector<Number>::iterator it = primes.begin(); it != primes.end(); ++it) {
		if (it->isPrime) {
			++i;
			if (i == xth+2)
				cout << it->value << endl;
		}
	}
}
