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

/*
    start 에서 시작해서 BFS 한 뒤 start 부터 각 정점까지
    최단거리와 BFS spanning tree 계산.
    distance[i] = start ~ i 거리
    parent[i] = BFS spanning tree에서 i의 부모 번호.
    root인 경우 자신의 번호
*/

void bfs2(int start, vector<int>& distance, vector<int>& parent){
    distance = vector<int>(adjList.size(), -1);
    parent = vector<int>(adjList.size(), -1);
    // 방문할 정점 목록 저장 큐
    queue<int> q;
    distance[start] = 0;
    parent[start] = start; // root
    q.push(start);
    while(!q.empty()){
        int cur = q.front();
        q.pop();
        // current node와 인접한 모든 정점 검사
        for(int i = 0; i < adjList[cur].size(); i++){
            int next = adjList[cur][i];
            // 최초 발견이면 방문 목록 큐에 push
            if(distance[next] == -1){
                q.push(next);
                // next 거리 = 지금까지의 거리(cur까지 거리) + 1
                distance[next] = distance[cur] + 1;
                parent[next] = cur;
            }
        }
    }
}

// v에서 시작점까지의 최단 경로
vector<int> shortestPath(int v, const vector<int>& parent){
    vector<int> path(1, v); // size 1이고 값으로 v를 갖는 벡터
    while(parent[v] != v){
        v = parent[v];
        path.push_back(v);
    }
    reverse(path.begin(), path.end());
    return path;
}
