#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int INF = 987654321, SWITCHES = 10, CLOCKS = 16;

/*
	연결상태를 문자열 배열에 저장
	x : 연결
	. : 연결 X
*/

const char linked[SWITCHES][CLOCKS + 1] = {
	"xxx.............",
	"...x...x.x.x....",
	"....x.....x...xx",
	"x...xxxx........",
	"......xxx.x.x...",
	"x.x...........xx",
	"...x..........xx",
	"....xx.x......xx",
	".xxxxx..........",
	"...xxx...x...x.."
};



bool check(const vector<int>& clocks) {
	for (int clock = 0; clock < CLOCKS; clock++) {
		if (clocks[clock] != 12) {
			return false;
		}
	}
	return true;
}

void pushSwitch(vector<int>& clocks, int swtch) {
	for (int clock = 0; clock < CLOCKS; clock++) {
		// 스위치와 연결되어있다면
		if (linked[swtch][clock] == 'x') {
			clocks[clock] += 3;
			// 만약 시계가 한바퀴를 다 돌았다면
			if (clocks[clock] == 15) {
				clocks[clock] = 3; // 12를 빼준다.
			}
		}
	}
}


int solve(vector<int>& clocks, int swtch) {
	/* 
		기저사례 : 모든 스위치를 조작한 후 
		모든 시계가 12시를 가리키는지 확인하고
		만약 그렇다면 0을(조작을 더이상 안해도 되므로)
		그렇지 않다면 INF(매우 큰 값)을 반환한다.
	*/ 
	if (swtch == SWITCHES) return check(clocks) ? 0 : INF;

	int ret = INF;
	for (int i = 0; i < 4; i++) {
		ret = min(ret, i + solve(clocks, swtch + 1));
		pushSwitch(clocks, swtch);
	}
	return ret;
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		vector<int> clock;
		int temp;
		for (int i = 0; i < 16; i++) {
			cin >> temp;
			clock.push_back(temp);
		}
		if (solve(clock, 0) == INF) cout << -1 << endl;
		else cout << solve(clock, 0) << endl;
	}
	return 0;
}