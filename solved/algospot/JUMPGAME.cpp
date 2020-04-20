#include <iostream>
#include <string.h>


/*
	������ȹ�� ����
*/

using namespace std;

int board[100][100]; // ������ ������ �迭
int cache[100][100]; 
int N;

int solve(int y, int x) {
	if (y >= N || x >= N) return 0; // �������� ����� ���
	
	if (y == N - 1 && x == N - 1) return 1; // �������� ������ ���
	
	int& ret = cache[y][x];
	if (ret != -1) return ret;

	int nextSize = board[y][x];
	return ret = (solve(y + nextSize, x) || solve(y, x + nextSize)); // �Ʒ��� �Ǵ� ���� �̵� ���ȣ��
}


int main() {
	int C;
	cin >> C;
	while (C--) {
		cin >> N;
		memset(cache, -1, sizeof(cache)); // cache �迭�� �� -1���� �ʱ�ȭ
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> board[i][j];
			}
		}
		solve(0, 0) ? cout << "YES" << endl : cout << "NO" << endl;
	}
}
	