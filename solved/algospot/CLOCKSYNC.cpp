#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
const int INF = 987654321, SWITCHES = 10, CLOCKS = 16;

/*
	������¸� ���ڿ� �迭�� ����
	x : ����
	. : ���� X
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
		// ����ġ�� ����Ǿ��ִٸ�
		if (linked[swtch][clock] == 'x') {
			clocks[clock] += 3;
			// ���� �ð谡 �ѹ����� �� ���Ҵٸ�
			if (clocks[clock] == 15) {
				clocks[clock] = 3; // 12�� ���ش�.
			}
		}
	}
}


int solve(vector<int>& clocks, int swtch) {
	/* 
		������� : ��� ����ġ�� ������ �� 
		��� �ð谡 12�ø� ����Ű���� Ȯ���ϰ�
		���� �׷��ٸ� 0��(������ ���̻� ���ص� �ǹǷ�)
		�׷��� �ʴٸ� INF(�ſ� ū ��)�� ��ȯ�Ѵ�.
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