#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	int score[1000] = { 0 };
	for (int i = 0; i < n; i++) {
		cin >> score[i];
	}
	int max = score[0];
	for (int i = 0; i < n; i++) {
		if (max < score[i]) {
			max = score[i];
		}
	}
	float arr[1000] = { 0 };
	float sum = 0;
	for (int i = 0; i < n; i++) {
		arr[i] = (score[i] /(float) max * 100);
		sum += arr[i];
	}
	cout << sum / n;
	return 0;
}