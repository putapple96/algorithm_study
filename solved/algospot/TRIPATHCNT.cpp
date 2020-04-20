#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int triangle[101][101];
int n;
int cache[100][100];
int pathCache[100][100];

int getPath(int y, int x) {
	if (y == n - 1) return triangle[y][x];
	int& ret = pathCache[y][x];
	if (ret != -1) return ret;
	return ret = max(getPath(y + 1, x), getPath(y + 1, x + 1)) + triangle[y][x];
}

int solve(int y, int x) {
	if (y == n - 1) return 1;
	int& ret = cache[y][x];
	if (ret != -1) return ret;
	ret = 0;
	if (getPath(y + 1, x) >= getPath(y + 1, x + 1)) ret += solve(y + 1, x);
	if (getPath(y + 1, x) <= getPath(y + 1, x + 1)) ret += solve(y + 1, x + 1);
	return ret;
}

int main() {
	int tc;
	cin >> tc;
	while (tc--) {
		cin >> n;
		memset(cache, -1, sizeof(cache));
		memset(pathCache, -1, sizeof(cache));
		for (int i = 0; i < n; i++) {
			for (int j = 0; j <= i; j++) {
				cin >> triangle[i][j];
			}
		}
		cout << solve(0, 0) << endl;
	}
}