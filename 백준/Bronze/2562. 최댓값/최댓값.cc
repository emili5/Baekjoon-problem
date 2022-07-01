#include <iostream>
using namespace std;
int main() {
	int n;
	int max = -1000000;
	int k;
	for (int i = 0; i < 9; i++) {
		cin >> n;
		if (max < n) {
			max = n;
			k = i + 1;
		}
	}
		cout << max << endl << k;
	return 0;
}