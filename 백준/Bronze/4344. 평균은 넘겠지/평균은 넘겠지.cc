#include <iostream>
using namespace std;
int main() {
	int c, n, v[1001];
	cin >> c;
	int sum;
	float avg = 0;
	int cnt;
	float result;
	for (int i = 0; i < c; i++) {
		cin >> n;
		sum = 0;
		cnt = 0;//초기화 반드시!!
		for (int j = 0; j < n; j++) {
			cin >> v[j];
			sum += v[j];
		}
		avg = sum / n;
		for (int j = 0; j < n; j++) {
			if (avg < v[j]) {
				cnt++;
			}
		}
		//소수점 자리수 고정하기
		result = cnt / (float)n * 100;
		cout<<fixed;
		cout.precision(3);
		cout<< result<< "%" << endl;
	}
	
	return 0;
}