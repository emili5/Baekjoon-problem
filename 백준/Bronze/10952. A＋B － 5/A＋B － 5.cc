#include <iostream>
using namespace std;
int main() {
	int a, b;
	for (int i = 0; i < 1000; i++) {
		cin >> a >> b;
		if (a == 0 && b == 0) break;
		cout << a + b << '\n';
	}
	return 0;
}