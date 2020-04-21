#include <iostream>
using namespace std;

/*
	�����佺�׳׽��� ü
	cout ���� ��� �� �ð��ʰ�!
	input method �� ���� �ð� ��
	��ũ : https://algospot.com/forum/read/2496/
*/
int main() {
	int n, m;
	cin >> n >> m;
	int* num = new int[m + 1];
	num[1] = 0;
	for (int i = 2; i <= m; i++) {
		num[i] = i;
	}
	for (int i = 2; i*i<= m; i++) { // sqrt(m) ������ Ž���ϸ� �ȴ�.
		if (num[i] == 0) continue;
		for (int j = 2 * i; j <= m; j += i) {
			num[j] = 0;
		}
	}
	for (int i = n; i <= m; i++) {
		if (num[i] != 0) printf("%d\n", num[i]);
	}
}