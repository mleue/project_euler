#include <iostream>
#include <vector>

using namespace std;

void fibonacciSum(int a, int b, const int &threshold, vector<int> &fib) {
	int c = a + b;
	if (c < threshold) {
		fib.push_back(c);
		fibonacciSum(b, c, threshold, fib); 
	}
	else
		return;
}

int main() {
	int threshold = 4000000;
	vector<int> fib;
	fib.push_back(1);
	fib.push_back(2);

	fibonacciSum(1, 2, threshold, fib);


	int sum = 0;
	for(vector<int>::iterator it = fib.begin(); it != fib.end(); ++it) {
		if (*it%2 == 0)
			sum += *it;
	}

	cout << "The sum of all even valued Fibonacci numbers below 4.000.000 is " << sum << endl;
}
