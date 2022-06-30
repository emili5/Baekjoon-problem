#include <iostream>
using namespace std;
int main() {
	int score;
	cin >> score;
	char res;
	if (score >= 90 && score <= 100) {
		res = 'A';
	}
	else if (score >= 80) {
		res = 'B';
	}
	else if (score >= 70) {
		res = 'C';
	}
	else if (score >= 60) {
		res = 'D';
	}
	else {
		res = 'F';
	}
	cout << res;
	return 0;
}