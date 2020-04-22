#include <bits/stdc++.h>

using namespace std;


vector<vector<int> > adjList;

vector<bool> visited;

void dfs(int cur){
    visited[cur] = true;
    for(int i = 0; i < adjList[cur].size(); i++){
        int next = adjList[next][i];

        if(!visited[next]) dfs(next);
    }
}

// 서로 연결되지 않은 그래프가 존재할 경우 
// dfsAll을 통해 모든 정점을 다 방문하여 dfs

void dfsAll(){
    visited = vector<bool>(adjList.size(), false);
    for(int i = 0; i < adjList.size(); i++){
        if(!visited[i]){
            dfs(i);
        }
    }
}