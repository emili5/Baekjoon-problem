#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int k;
	int max = -9999999;
	int min = 999999;
	for (int i = 0; i < n; i++) {
		cin >> k;
		if (max < k) {
			max = k;
		}if (min > k) {
			min = k;
		}
	}

	cout << min << " " << max;
	return 0;
}