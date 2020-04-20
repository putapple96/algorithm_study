#include <iostream>
#include <string.h>


/*
	동적계획법 기초
*/

using namespace std;

int board[100][100]; // 게임판 저장할 배열
int cache[100][100]; 
int N;

int solve(int y, int x) {
	if (y >= N || x >= N) return 0; // 게임판을 벗어나는 경우
	
	if (y == N - 1 && x == N - 1) return 1; // 도착점에 도달한 경우
	
	int& ret = cache[y][x];
	if (ret != -1) return ret;

	int nextSize = board[y][x];
	return ret = (solve(y + nextSize, x) || solve(y, x + nextSize)); // 아래쪽 또는 우측 이동 재귀호출
}


int main() {
	int C;
	cin >> C;
	while (C--) {
		cin >> N;
		memset(cache, -1, sizeof(cache)); // cache 배열의 값 -1으로 초기화
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> board[i][j];
			}
		}
		solve(0, 0) ? cout << "YES" << endl : cout << "NO" << endl;
	}
}
	