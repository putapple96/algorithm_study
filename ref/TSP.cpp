/*
	여행하는 외판원 문제(완전탐색)
*/

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 10
#define INF 987654321

using namespace std;

int n; // 도시 수
double dist[MAX][MAX]; // 도시간의 거리를 저장할 이차원 배열

/* 
	path : 현재까지의 거리 저장
	visited : 각 도시 방문 여부
	currentLength : 현재까지 경로의 길이
*/
double shortestPath(vector<int>& path, vector<bool>& visited, double currentLength) {
	// 기저사례 : 모든 도시를 방문하였으면
	// 시작점으로 돌아가는 경로의 길이를 더해준 값 반환
	if (path.size() == n) {
		return currentLength + dist[path[0]][path.back()];
	}
	double ret = INF;

	for (int next = 0; next < n; next++) {
		if (visited[next]) continue;
		int curPos = path.back(); // 현재 도시 위치 저장
		path.push_back(next); 
		visited[next] = true;

		double candi = shortestPath(path, visited, currentLength + dist[curPos][next]);
		// 재귀함수로 경로의 길이를 구한다
		ret = min(ret, candi); // 현재 ret 값과 비교하여 더 작은 값을 ret에 저장
		visited[next] = false; // 새로운 경로를 찾기 위해 next의 방문여부를 false로 바꾸어주고 경로에서 pop 해줌
		path.pop_back();
	}
	return ret;
}
