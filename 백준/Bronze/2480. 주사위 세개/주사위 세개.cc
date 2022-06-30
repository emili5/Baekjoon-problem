#include <iostream>
using namespace std;
int main() {
	int a, b, c;
	cin >> a >> b >> c;
	int mon = 0;
	if (a == b && a == c && b == c) {
		mon = 10000 + a * 1000;
	}
	else if (a == b) {
		mon = 1000 + a * 100;
	}
	else if (b == c) {
		mon = 1000 + b * 100;
	}
	else if (a == c) {
		mon = 1000 + c * 100;
	}
	else {
		if (a > b && a > c) {
			mon = a * 100;
		}
		else if (b > a && b > c) {
			mon = b * 100;
		}
		else {
			mon = c * 100;
		}
	}
	cout << mon;

	return 0;
}