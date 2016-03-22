#include <vector>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main() {
	vector< vector<int> > rows;

	ifstream file("../numberTriangle.txt");

	if (!file) {
		cout << "unable to open file" << endl;
		return 0;
	}

	std::string s;
	int numbersPerLine = 1;
	while (std::getline(file, s))
	{
		vector<int> row;
		//TODO ugly read in code and put it into separate function
		for (int i = 0; i < numbersPerLine*3; i=i+3) {
			int value = (s[i] - '0')*10+(s[i+1] - '0');
			row.push_back(value);
		}
		rows.push_back(row);
		++numbersPerLine;
	}
	file.close();

	//TODO super ugly sum up code and put it into separate function
	for (int i=rows.size()-1; i>0; --i) {
		for (int j=0; j<rows[i-1].size(); ++j) {
			rows[i-1][j] = rows[i-1][j]+rows[i][j] > rows[i-1][j]+rows[i][j+1] ? rows[i-1][j]+rows[i][j] : rows[i-1][j]+rows[i][j+1]; 
		}
	}

	cout << "The max sum of the given triangle is: " << rows[0][0] << endl;
}

