#include <iostream>

using namespace std;

long addDigitToInt(long old, int digit) {
	old *= 10;
	return (old+digit);
}

long reverseInt(long original) {
	long reverse = 0;

	while (original != 0) {
		int digit = original%10;
		reverse = addDigitToInt(reverse, digit);
		original -= digit;
		original /= 10;
	}

	return reverse;
}

bool isPalindrome(long number) {
	if (number == reverseInt(number))
		return true;
	else
		return false;
}

int main() {
	long largest = 0;

	for (int i = 999; i > 99; --i) {
		for (int j = 999; j > 99; --j) {
			long current = i*j;
			if (isPalindrome(current))
				largest = current > largest ? current : largest;
		}
	}
	cout << "The largest palindrome from the multiplication of two 3-digit numbers is: " << largest << endl;
}
