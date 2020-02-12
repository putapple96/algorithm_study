#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int solve(int left, int right, vector<int> woods) {
	int mid = (left + right) / 2; // �߰� ���� �������� ���� ����
	// ���� : ���ڰ� �ϳ��ۿ� �ȳ����� ���
	if (left == right) return woods[left];

	// case1 : ���ʰ� �������� ���� �� ������ ������� �ִ밪�� ���Ѵ�.
	int ret = max(solve(left, mid, woods), solve(mid + 1, right, woods));

	// case2 : �߰� ���ڸ� �����ϴ� ��� -> ����, ������ ���̸� �ִ�ȭ �ϴ� ������ Ȯ���Ų��.
	int first = mid, second = mid + 1; // �ϴ� ���������� Ȯ���� ����
	int height = min(woods[first], woods[second]); 
	ret = max(ret, height * 2); // Ȯ���� �ʺ� 2�� ���簢���� ������ ���� �������� ���� ���� ���Ͽ� �� ū������ ret ���� ����

	while (left < first || second < right) { // ��� �������ڿ� ���� Ž��
		if (second < right && (first == left || woods[first - 1] < woods[second + 1])) {
			/* 
				1. ���������� �� Ȯ�尡���ϰ�
				2. �������� ���̻� Ȯ�� �Ұ��ɰų�
				 3. ���ʺ��� ���������� Ȯ���ϴ� ���̰� �� ���� ��
			 */
			second++;// ���������� ��ĭ �̵����ְ�
			height = min(height, woods[second]); // ���� ������Ʈ
		}
		else { // ���� ���� �ݴ��� ��
			first--;
			height = min(height, woods[first]);
		}
		ret = max(ret, height * (second - first + 1));
	}
	return ret;
}

int main() {
	int C;
	int temp;
	cin >> C;
	while (C--) {
		int N;
		cin >> N;
		vector<int> w;
		for (int i = 0; i < N; i++) {
			cin >> temp;
			w.push_back(temp);
		}
		cout << solve(0, w.size()-1, w) << endl;
	}
}