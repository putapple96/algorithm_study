#include <iostream>
#define MAX 101

using namespace std;
int node[MAX][MAX];
bool visited[MAX] = { false, };

int c, n; // # of computer, # of computer pair

void dfs(int curNode) {
	visited[curNode] = true;
	for (int i = 1; i <= c; i++) {
		if (visited[i] || node[curNode][i] == 0) continue;
		else dfs(i);
	}
}

int main() {	
	cin >> c;
	cin >> n;
	int ans = 0;
	while (n--) {
		int a, b; 
		cin >> a >> b;
		node[a][b] = 1; node[b][a] = 1;
	}
	dfs(1);
	for (int i = 2; i <= c; i++) {
		if (visited[i]) ans++;
	}
	cout << ans;
	return 0;
}
