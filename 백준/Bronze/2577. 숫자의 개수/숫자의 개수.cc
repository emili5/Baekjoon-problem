#include <iostream>
using namespace std;
int main() {
	int a, b, c;
	cin >> a >> b >> c;
	int res = a * b * c;
	int v[10] = { 0 };
	int t;
	for (int i = 100000; i < 1000000000; i*=10) {
		if (res / i > 0 && res / i < 10) {
			t = i;
		}
	}
	
	for (int i = 0; i < 10; i++) {
		v[res / t] += 1;
		res %= t;
		t /= 10;
		if (t == 0) break;
	}
	for (int i = 0; i < 10; i++) {
		cout << v[i] << endl;
	}
	return 0;
}