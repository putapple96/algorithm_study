#include <iostream>
using namespace std;

/*
	에라토스테네스의 체
	cout 으로 출력 시 시간초과!
	input method 별 실행 시간 비교
	링크 : https://algospot.com/forum/read/2496/
*/
int main() {
	int n, m;
	cin >> n >> m;
	int* num = new int[m + 1];
	num[1] = 0;
	for (int i = 2; i <= m; i++) {
		num[i] = i;
	}
	for (int i = 2; i*i<= m; i++) { // sqrt(m) 까지만 탐색하면 된다.
		if (num[i] == 0) continue;
		for (int j = 2 * i; j <= m; j += i) {
			num[j] = 0;
		}
	}
	for (int i = n; i <= m; i++) {
		if (num[i] != 0) printf("%d\n", num[i]);
	}
}