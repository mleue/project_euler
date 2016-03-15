#include <vector>
#include <iostream>

class ProductGrid
{
	int size;
	long maxProduct;
	std::vector< std::vector<int> > grid;
	int l;

public:
	ProductGrid(std::vector< std::vector<int> > &grid, int size) 
		:size(size),
		grid(grid),
		maxProduct(0),
		l(0)
	{
	}

	//TODO double evaluation
	//TODO should we really set member variables in this public function?
	long getMaxProduct(int limit) {
		maxProduct = 0;
		l = limit;
		for (int i=0; i<size; ++i) {
			for (int j=0; j<size; ++j) {
				maxProduct = downProduct(i,j) > maxProduct ? downProduct(i,j) : maxProduct;
				maxProduct = rightProduct(i,j) > maxProduct ? rightProduct(i,j) : maxProduct;
				maxProduct = diagrProduct(i,j) > maxProduct ? diagrProduct(i,j) : maxProduct;
				maxProduct = diaglProduct(i,j) > maxProduct ? diaglProduct(i,j) : maxProduct;
			}
		}

		return maxProduct;
	}

private:
	long downProduct(int i, int j) {
		if (i+l > size-1)
			return 0;
		else {
			long product = 1;
			for (int k=i; k<i+l; ++k) {
				product *= grid[k][j];
			}
			return product;
		}
	}

	long rightProduct(int i, int j) {
		if (j+l > size-1)
			return 0;
		else {
			long product = 1;
			for (int k=j; k<j+l; ++k) {
				product *= grid[i][k];
			}
			return product;
		}
	}

	long diagrProduct(int i, int j) {
		if (j+l > size-1 || i+l > size-1)
			return 0;
		else {
			long product = 1;
			for (int k=0; k<l; ++k) {
				int a = i+k;
				int b = j+k;
				product *= grid[a][b];
			}
			return product;
		}
	}

	//TODO comparison correct? <0 or <1?
	long diaglProduct(int i, int j) {
		if (j-l < 0 || i+l > size-1)
			return 0;
		else {
			long product = 1;
			for (int k=0; k<l; ++k) {
				int a = i+k;
				int b = j-k;
				product *= grid[a][b];
			}
			return product;
		}
	}
};
