#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solve(string& s, int idx) {
	char cur = s[idx];
	if (cur == 'w' || cur == 'b') {
		return string(1,cur); // char ���� string ������ ��ȯ
	}
	// idx��ġ�� ���ڰ� w,b �� �ƴϸ� x�̴�. �ε����� 1 ���������ְ�
	// ������, ��������,  ���ʾƷ�, ������ �Ʒ� ������ ����Լ� ȣ�����ش�.
	idx++; 
	string upLeft = solve(s, idx);
	idx += upLeft.size(); // �������� ������ string�� ���̸�ŭ �ε����� �����ش�. ���� ����
	string upRight = solve(s, idx);
	idx += upRight.size();
	string downLeft = solve(s, idx);
	idx += downLeft.size();
	string downRight = solve(s, idx);
	// ���Ϸ� ������� �ϹǷ�, ������ �κ��� ������ �͵��� ���� �Ʒ��� ��ġ�� �ٲپ� ��ȯ���ش�.
	return 'x' + downLeft + downRight + upLeft + upRight; 
}

int main() {
	int C;
	cin >> C;
	while (C--) {
		string tree;
		cin >> tree;
		cout << solve(tree, 0) << endl;
	}
}