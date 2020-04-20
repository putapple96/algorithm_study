#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int solve(int left, int right, vector<int> woods) {
	int mid = (left + right) / 2; // 중간 판자 기준으로 분할 정복
	// 기저 : 판자가 하나밖에 안남았을 경우
	if (left == right) return woods[left];

	// case1 : 왼쪽과 오른쪽을 나눈 후 각각의 결과에서 최대값을 구한다.
	int ret = max(solve(left, mid, woods), solve(mid + 1, right, woods));

	// case2 : 중간 판자를 포함하는 경우 -> 좌측, 우측중 높이를 최대화 하는 쪽으로 확장시킨다.
	int first = mid, second = mid + 1; // 일단 오른쪽으로 확장을 시작
	int height = min(woods[first], woods[second]); 
	ret = max(ret, height * 2); // 확장한 너비가 2인 직사각형과 위에서 분할 정복으로 구한 값을 비교하여 더 큰값으로 ret 값에 저장

	while (left < first || second < right) { // 모든 나무판자에 대해 탐색
		if (second < right && (first == left || woods[first - 1] < woods[second + 1])) {
			/* 
				1. 오른쪽으로 더 확장가능하고
				2. 왼쪽으로 더이상 확장 불가능거나
				 3. 왼쪽보다 오른쪽으로 확장하는 높이가 더 넓을 때
			 */
			second++;// 오른쪽으로 한칸 이동해주고
			height = min(height, woods[second]); // 높이 업데이트
		}
		else { // 위의 경우와 반대일 때
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