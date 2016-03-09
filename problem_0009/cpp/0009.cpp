#include <cmath>
#include <iostream>

bool pythagoreanTriplet(int &a, int &b, int &c, int sum) {
	for (a=1; a<(sum/3); ++a) {
		for (b=a; b<(sum/2); ++b) {
			//check if the root is actually an integer value
			float root = std::sqrt(a*a + b*b);
			if (floor(root) == root)
				c = root;
			else 
				continue;

			int checksum = a+b+c;
			if (checksum == sum && b<c)
				return true;
		}
	}
	return false;
}

int main() {
	int a,b,c = 1;
	int sum = 1000;
	if (pythagoreanTriplet(a,b,c,sum))
		std::cout << "The product of the pythagorean triplet that sums up to 1000 is: " << a*b*c << std::endl;
	else
		std::cout << "No pythagorean triplet that sums up to 1000 could be found" << std::endl;
}
