#include <iostream>
using namespace std;
int main() {
	int h, m;
	cin >> h >> m;
	m -= 45;
	if (m < 0) {
		if (h != 0) h--;
		else h = 23;

		m += 60;
	}
	
	cout << h << " " << m;
	return 0;
}