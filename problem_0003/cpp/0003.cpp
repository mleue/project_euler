#include <iostream>

using namespace std;

void largestPrimeFactor(long number, long &largestDivisor) {
	for (long i=2; i<=number; ++i) {
		if (number%i == 0) {
			largestDivisor = i > largestDivisor ? i : largestDivisor;
			if (number != i) {
				largestPrimeFactor(number/i, largestDivisor);
				break;
			}
			else {
				return;
			}
		}
	}
}

int main() {
	long number = 600851475143;
	long largestDivisor = 1;

	largestPrimeFactor(number, largestDivisor);

	cout << "The largest prime factor in " << number << " is " << largestDivisor << endl;
}
