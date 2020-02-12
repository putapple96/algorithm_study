#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solve(string& s, int idx) {
	char cur = s[idx];
	if (cur == 'w' || cur == 'b') {
		return string(1,cur); // char 형을 string 형으로 변환
	}
	// idx위치의 문자가 w,b 가 아니면 x이다. 인덱스를 1 증가시켜주고
	// 왼쪽위, 오른쪽위,  왼쪽아래, 오른쪽 아래 순으로 재귀함수 호출해준다.
	idx++; 
	string upLeft = solve(s, idx);
	idx += upLeft.size(); // 왼쪽위가 리턴한 string의 길이만큼 인덱스를 더해준다. 이하 동일
	string upRight = solve(s, idx);
	idx += upRight.size();
	string downLeft = solve(s, idx);
	idx += downLeft.size();
	string downRight = solve(s, idx);
	// 상하로 뒤집어야 하므로, 각각의 부분을 뒤집은 것들의 위와 아래의 위치를 바꾸어 반환해준다.
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