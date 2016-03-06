#include <iostream>

int main() {
	int i = 2520;
	bool smallestMultipleFound = false;

	while (!smallestMultipleFound) {
		if (i%11 == 0 && i%12 == 0 && i%13 == 0 && i%14 == 0 && i%15 == 0
				&& i%16 == 0 && i%17 == 0 && i%18 == 0 && i%19 == 0)
			smallestMultipleFound = true;
		else
			i += 20;
	}

	std::cout << "The smallest number that can be evenly divided by all numbers from 1..20 is: " << i << std::endl;
}
