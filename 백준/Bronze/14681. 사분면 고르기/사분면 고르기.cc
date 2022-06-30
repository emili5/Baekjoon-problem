#include <iostream>
using namespace std;
int main() {
	int x, y;
	cin >> x >> y;
	int res;
	if (y > 0) {
		if (x > 0) {
			res = 1;
		}
		else {
			res = 2;
		}
	}
	else {
		if (x <0) {
			res = 3;
		}
		else {
			res = 4;
		}
	}
	cout << res;
	return 0;

}