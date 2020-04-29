#include <bits/stdc++.h>

using namespace std;

// 인접 리스트
vector<vector<int> > adjList;

// bfs 함수는 start 에서 시작하여 너비우선 탐색 후 각 정점의 방문 순서 반환
vector<int> bfs(int start){
    // 각 정점 방문 여부
    vector<bool> visited(adjList.size(), false);
    // 방문할 정점 저장할 큐
    queue<int> q;
    // 정점 방문 순서
    vector<int> order;
    visited[start] = true;
    q.push(start);
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        // cur 방문
        order.push_back(cur);
        // 모든 인접 정점 검사
        for(int i = 0; i < adjList[cur].size(); i++){
            int next = adjList[cur][i];
            // 방문 하지 않았던 정점이면 방문할 목록 큐에 저장
            if(!visited[next]){
                q.push(next);
                visited[next] = true;
            }
        }
    }
    return order;
}