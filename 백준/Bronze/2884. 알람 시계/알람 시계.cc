#include <iostream>
using namespace std;
int main() {
	int h, m;
	cin >> h >> m;
	if (m - 45 < 0) {
		if (h != 0) {
			h--;
		}
		else {
			h = 23;
		}
		m += 60;
		m -= 45;
	}
	else {
		m -= 45;
	}
	cout << h << " " << m;
	return 0;
}