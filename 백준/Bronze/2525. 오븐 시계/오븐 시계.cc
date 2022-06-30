#include <iostream>
using namespace std;
int main() {
	int h, m, t;
	
	cin >> h >> m >> t;
	
	m = m + t;
	if (m-60>= 0) {
		int k = m / 60;
		h += k;
		m%= 60;
	}
	if (h > 23) h -= 24;
	cout << h << " " << m;

	return 0;
}