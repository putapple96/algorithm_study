#include <iostream>

using namespace std;

bool areFriend[10][10]; // 서로 친구인지 여부를 나타내는 2차원 배열


int n, m;

int solve(bool completed[10]) {
	int head = -1; // 가장 번호 빠른 학생 찾기
	for (int i = 0; i < 10; ++i) {
		if (!completed[i]) {
			head = i;
			break;
		}
	}
	if (head == -1) return 1; // 기저 : 모든 학생이 짝을 찾은 경우
	int ret = 0;
	// head 학생과 짝을 지을 학생을 찾는다
	for (int pairWith = head + 1; pairWith < n; ++pairWith) {
		if (!completed[pairWith] && areFriend[head][pairWith]) {
			completed[pairWith] = completed[head] = true;
			ret += solve(completed);
			completed[pairWith] = completed[head] = false;
		}
	}
	return ret;
}

int main() {
	int C;
	bool completed[10]; // 짝을 지었는지 여부를 나타내는 2차원 배열
	cin >> C;
	while (C--) {
		
		cin >> n >> m; // n : 학생 수, m : 친구 쌍의 수

		memset(areFriend, false, sizeof(areFriend));
		memset(completed, false, sizeof(completed));

		for (int i = 0; i < m; ++i) {
			int first, second;
			areFriend[first][second] = areFriend[second][first] = true;
		}
		cout << solve(completed) << endl;
	}
}
