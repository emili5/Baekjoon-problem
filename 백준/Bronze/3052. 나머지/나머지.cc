#include <iostream>
using namespace std;
int main() {
	int v[10];
	for (int i = 0; i < 10; i++) {
		cin >> v[i];
	}
	int arr[1000] = { 0 };
	int t = 0;
	for (int i = 0; i < 10; i++) {
		t = v[i] % 42;
		arr[t]++;
	}
	int cnt = 0;
	for (int i = 0; i < 1000; i++) {
		if (arr[i] != 0) cnt++;
	}
	cout << cnt;
	return 0;
}