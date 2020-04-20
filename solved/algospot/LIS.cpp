#include <iostream>
#include <algorithm>
#include <cstring> // memset

using namespace std;

int c;
int n;
int dp[500], arr[500];

int solve(int s) {
	int& ret = dp[s];
	if (ret != -1) return ret;
	ret = 1;
	for (int idx = s + 1; idx < n; idx++) {
		if (arr[s] < arr[idx])
			ret = max(ret, solve(idx) + 1);
	}
	return ret;
}


int main() {
	cin >> c;
	while (c--) {
		cin >> n;
		memset(dp, -1, sizeof(dp));
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
		}
		int len = 0;
		for (int i = 0; i < n; i++) {
			len = max(len, solve(i));
		}
		cout << len << endl;
	}
}