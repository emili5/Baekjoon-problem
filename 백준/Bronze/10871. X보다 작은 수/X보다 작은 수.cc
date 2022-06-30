#include <iostream>
using namespace std;
int main() {
	int n, a;
	cin >> n >> a;
	int b;
	for (int i = 0; i < n; i++) {
		cin >> b;
		if (a > b) cout << b << " ";
	}
	return 0;
}