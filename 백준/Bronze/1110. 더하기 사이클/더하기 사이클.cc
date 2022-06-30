#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int cnt = 0;
	int t = n;
	while (1) {
		int a = ((n % 10) + (n / 10)) % 10;
		int b = (n % 10);
		n= b * 10 + a;
		cnt++;
		if (t == n) break;
	}
	cout << cnt;
	return 0;
}