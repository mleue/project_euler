#include <vector>

/* Column class containing an integer column to add to the sum */
class Column {
	std::vector<int> column;
	int tenner;
	int carry_to;
	int carry_from;

public:
	Column(std::vector<int> &c)
		:column(c),
		tenner(0),
		carry_to(0),
		carry_from(0)
	{
	}
	
	int getTenner() {
		return tenner;
	}

	int getCarryFrom() {
		return carry_from;
	}

	void setCarryTo(int carry) {
		carry_to = carry;
		calculateSum();
	}

private:
	void calculateSum() {
		int sum = carry_to;
		for(std::vector<int>::iterator it = column.begin(); it != column.end(); ++it) {
			sum += *it;
		}
		tenner = sum%10;
		carry_from = (sum-tenner)/10;
	}
};
