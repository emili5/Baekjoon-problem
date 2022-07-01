#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	char v[21];
	int t;
	
	int len = 0;
	for (int i = 0; i < n; i++) {
		cin >> t >> v;
		for (int j = 0; j < 21; j++) {
			if (v[j] == '\0') {
				len = j;
				break;
			}
		 }
		for (int j = 0; j < len; j++) {
			for (int k = 0; k < t; k++) {
				cout << v[j];
			}
		}cout << endl;
	}
	
	return 0;
}