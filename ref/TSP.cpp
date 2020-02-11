/*
	�����ϴ� ���ǿ� ����(����Ž��)
*/

#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 10
#define INF 987654321

using namespace std;

int n; // ���� ��
double dist[MAX][MAX]; // ���ð��� �Ÿ��� ������ ������ �迭

/* 
	path : ��������� �Ÿ� ����
	visited : �� ���� �湮 ����
	currentLength : ������� ����� ����
*/
double shortestPath(vector<int>& path, vector<bool>& visited, double currentLength) {
	// ������� : ��� ���ø� �湮�Ͽ�����
	// ���������� ���ư��� ����� ���̸� ������ �� ��ȯ
	if (path.size() == n) {
		return currentLength + dist[path[0]][path.back()];
	}
	double ret = INF;

	for (int next = 0; next < n; next++) {
		if (visited[next]) continue;
		int curPos = path.back(); // ���� ���� ��ġ ����
		path.push_back(next); 
		visited[next] = true;

		double candi = shortestPath(path, visited, currentLength + dist[curPos][next]);
		// ����Լ��� ����� ���̸� ���Ѵ�
		ret = min(ret, candi); // ���� ret ���� ���Ͽ� �� ���� ���� ret�� ����
		visited[next] = false; // ���ο� ��θ� ã�� ���� next�� �湮���θ� false�� �ٲپ��ְ� ��ο��� pop ����
		path.pop_back();
	}
	return ret;
}
