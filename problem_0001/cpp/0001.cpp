#include <vector>
#include <iostream>

using namespace std;
int main() {
	int n1 = 3;
	int n2 = 5;
	vector<int> multi;

	for (int i = 1; i < 1000; ++i) {
		if (i%n1 == 0 || i%n2 == 0)
			multi.push_back(i);
	}

	int sum = 0;
	for(vector<int>::iterator it = multi.begin(); it != multi.end(); ++it) {
		sum += *it;
	}

	cout << "The sum of all multiples of 3 and 5 below 1000 is " << sum << endl;
}
