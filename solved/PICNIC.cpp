#include <iostream>

using namespace std;

int n;
bool areFriends[10][10]; 

// taken[i] 는 i번째 학생이 짝을 찾았는가

int countPairings(bool taken[10]) {
	int firstStudent = -1;

	for (int i = 0; i < n; i++) {
		if (!taken[i]) {
			firstStudent = i;
			break;
		}
	}
	if (firstStudent == -1) return 1;
	int ret = 0;
	for (int p = firstStudent + 1; p < n; p++) {
		if (!taken[p] && areFriends[firstStudent][p]) {
			taken[firstStudent] = taken[p] = true;
			ret += countPairings(taken);
			taken[firstStudent] = taken[p] = false;
		}
	}
	return ret;
}

int main() {
	int test;
	bool taken[10];

	cin >> test;
	if (test < 0 || test > 50) exit(-1);
	for (int i = 0; i < test; i++) {
		int pair;
		cin >> n >> pair;
		memset(areFriends, false, sizeof(areFriends));
		memset(taken, false, sizeof(taken));

		for (int j = 0; j < pair; j++) {
			int s1, s2;
			cin >> s1 >> s2;
			areFriends[s1][s2] = areFriends[s2][s1] = true;
		}
		cout << countPairings(taken) << endl;
	}
}