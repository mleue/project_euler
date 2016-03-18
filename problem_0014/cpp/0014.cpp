#include <iostream>

using namespace std;

int collatzSequenceLength(long number) {
	int length = 1;
	while (number != 1) {
		number = number%2 == 0 ? (number/2) : (3*number + 1);
		++length;
	}
	return length;
}

int main() {
	int threshold = 999999;
	int max_collatz_length = 1;
	int max_seed = 1;
	for (long i=threshold; i>0; i-=2) {
		int current_collatz_length = collatzSequenceLength(i);
		if (max_collatz_length < current_collatz_length) {
			max_collatz_length = current_collatz_length;
			max_seed = i;
		}
	}

	cout << "The seed of all numbers under 1mio to create the longest collatz"
	   " sequence is: " << max_seed << " with a length of: " << max_collatz_length << endl;
}
