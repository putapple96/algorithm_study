#include <bits/stdc++.h>

using namespace std;

// 인접행렬. adj[i][j] = i와 j 사이 간선의 수
vector<vector<int> > adj;
vector<int> circuit;
// 무향 그래프에 대해
void eulerCircuit(int cur, vector<int>& circuit){
    for(int next = 0; next < adj[cur].size(); next++){
        while(adj[cur][next] > 0){
            adj[cur][next]--;
            adj[next][cur]--;
            eulerCircuit(next, circuit);
        }
    }
    circuit.push_back(cur);
}
// eulerCircuit 에서 구한 circuit 을 뒤집어 주어야 한다.
void getEulerCircuit(vector<int>& circuit){
    reverse(circuit.begin(), circuit.end());
}
