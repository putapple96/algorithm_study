#include <iostream>
#include <cstring> // memset

#define MAX_N 1000

using namespace std;

double dp[MAX_N][MAX_N * 2 + 1];

int n, m;

double solve(int day, int climbed) {
	if (day == m) return climbed >= n ? 1 : 0;

	double& ret = dp[day][climbed];
	if (ret != -1) return ret;
	return ret = 0.25 * solve(day + 1, climbed + 1) + 0.75 * solve(day + 1, climbed + 2);
}

int main() {
	int tc;
	cin >> tc;
	while (tc--) {
		cin >> n >> m;
		for (int i = 0; i < MAX_N; i++) {
			for (int j = 0; j < MAX_N * 2 + 1; j++)
				dp[i][j] = -1.0;
		}
		cout.precision(11);
		cout << solve(0, 0) << endl;
	}
}