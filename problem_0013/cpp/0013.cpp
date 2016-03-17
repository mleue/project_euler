#include "column.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	vector<Column> columns;

	ifstream file("../numbersTransposed.txt");

	if (!file) {
		cout << "unable to open file" << endl;
		return 0;
	}

	std::string s;
	while (std::getline(file, s))
	{
		vector<int> column_vec;
		for (int i = 0; i < 100; ++i) {
			column_vec.push_back(s[i] - '0');
		}
		columns.push_back(Column(column_vec));
	}
	file.close();

	int currentTenner = 0;
	int currentCarry = 0;
	string result = "";
	for (vector<Column>::reverse_iterator it = columns.rbegin(); it != columns.rend(); ++it) {
		it->setCarryTo(currentCarry);
		currentTenner = it->getTenner();
		currentCarry = it->getCarryFrom();
		result = std::to_string(currentTenner) + result;
	}
	result = std::to_string(currentCarry) + result;

	cout << "The sum of all columns is: " << result << endl;
}
