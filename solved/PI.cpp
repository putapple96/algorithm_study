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
	if (s == string(s.size(), s[0])) return 1; // ��� ���ڰ� ���� ��
	bool diffsame = true; // �������� ����
	for (size_t i = 0; i < s.size() - 1; i++) {
		if (s[i + 1] - s[i] != s[1] - s[0]) {
			diffsame = false; // ���������� �ƴϴ�.
			break;
		}
	}
	if (diffsame && abs(s[1] - s[0]) == 1) return 2; // ������ 1�� ��������
	bool change = true; // �� �� ������ ��Ÿ������ ����
	for (size_t i = 0; i < s.size(); i++) {
		if (s[i] != s[i % 2]) change = false;
	}

	if (change) return 4; // �� ���� ������ ����
	if (diffsame) return 5; // ���� 1 �ƴ� ��������
	
	return 10; // �� ���� ���
}

int solve(int s) {
	// base case : ���� ������ ���
	if (s == str.size()) return 0;

	int& ret = cache[s];
	if (ret != -1) return ret;
	ret = 987654321;
	for (size_t len = 3; len <= 5; len++) { // ���� 3 ~ 5 ���� ������ ���̵� + 3 ~ 5���� �� �������� ���� �ּ� ���̵� ��(������)
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