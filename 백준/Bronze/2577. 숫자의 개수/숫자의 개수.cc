#include <iostream>
using namespace std;
int main() {
	int a, b, c;
	cin >> a >> b >> c;
	int res = a * b * c;
	int v[10] = { 0 };
	//일의 자리부터 숫자 탐색-> 10으로 나눈 나머지
	//다음 자리 숫자 탐색-> 10으로 나누어 같은 과정 반복
	while (res > 0) {
		v[res % 10]++;
		res /= 10;
	}
	
	for (int i = 0; i < 10; i++) {
		cout << v[i] << endl;
	}
	return 0;
}