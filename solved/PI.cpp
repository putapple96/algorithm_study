#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int c;
string str;
int cache[10002];

int score(int b, int e) {
	string s = str.substr(b, e - b + 1);
	if (s == string(s.size(), s[0])) return 1; // 모든 숫자가 같을 때
	bool diffsame = true; // 등차수열 여부
	for (size_t i = 0; i < s.size() - 1; i++) {
		if (s[i + 1] - s[i] != s[1] - s[0]) {
			diffsame = false; // 등차수열이 아니다.
			break;
		}
	}
	if (diffsame && abs(s[1] - s[0]) == 1) return 2; // 공차가 1인 등차수열
	bool change = true; // 두 수 번갈아 나타나는지 여부
	for (size_t i = 0; i < s.size(); i++) {
		if (s[i] != s[i % 2]) change = false;
	}

	if (change) return 4; // 두 수가 번갈아 등장
	if (diffsame) return 5; // 공차 1 아닌 등차수열
	
	return 10; // 그 밖의 경우
}

int solve(int s) {
	// base case : 끝에 도달한 경우
	if (s == str.size()) return 0;

	int& ret = cache[s];
	if (ret != -1) return ret;
	ret = 987654321;
	for (size_t len = 3; len <= 5; len++) { // 길이 3 ~ 5 까지 조각의 난이도 + 3 ~ 5글자 뺀 나머지에 대한 최소 난이도 값(최적해)
		if (s + len <= str.size()) {
			ret = min(ret, solve(s + len) + score(s, s + len - 1));
		}
	}
	return ret;
}

int main() {
	cin >> c;
	while (c--) {
		cin >> str;
		memset(cache, -1, sizeof(cache));
		cout << solve(0) << endl;
	}
}