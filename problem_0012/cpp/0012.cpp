#include <iostream>

//TODO: this method takes like 10mins to run ;)
//TODO: think rather than brute force
long triangleNumberMoreThanLimitDivisors(int limit) {
	long triangleNumber = 0;
	int i = 1;
	while (true) {
		triangleNumber += i;
		int divisors = 0;
		for (int j=1; j<(triangleNumber+1)/2; ++j) {
			if (triangleNumber%j == 0)
				++divisors;
			if (j > triangleNumber/20 && divisors < limit/10)
				break;
		}
		if (divisors > limit-1)
			return triangleNumber;
		++i;
	}
}

int main() {
	int limit = 500;
	long triangleNumber = triangleNumberMoreThanLimitDivisors(limit);

	std::cout << "The first triangle number with more than " << limit << " divisors is: " << triangleNumber << std::endl;
}
