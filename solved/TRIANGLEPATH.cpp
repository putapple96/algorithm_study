#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int triangle[101][101];
int n;
int cache[101][101];

int solve(int y, int x) {
	if (y == n - 1) return triangle[y][x]; // ���� ��� : �� �ر��� �����Դٸ�
	int& ret = cache[y][x];
	if (ret != -1) return ret;
	return ret = max(solve(y + 1, x), solve(y + 1, x + 1)) + triangle[y][x]; // ��������� �ִ밪�� ��ȯ
}
int main() {
	int C;
	cin >> C;
	while (C--) {
		cin >> n;
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				cin >> triangle[i][j];
			}
		}
		memset(cache, -1, sizeof(cache));
		cout << solve(0, 0) << endl;
	}
}
