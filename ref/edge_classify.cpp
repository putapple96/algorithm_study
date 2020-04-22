#include <bits/stdc++.h>

using namespace std;

vector<vector<int> > adj;
// order[i] = i 발견순서, finished[i] = edgeClassify(i)의 종료여부. 1 true 0 false
vector<int> order, finished;
// 현재까지 찾은 정점의 수
int counter=0;

void edgeClassify(int cur){
    order[cur] = counter++;
    for(int i =0; i < adj[cur].size(); i++){
        int next = adj[cur][i];
        if(order[next] == -1){
            printf("Tree Edge : (%d, %d)\n", cur, next);
            edgeClassify(next);
        }
        else if(order[cur] < order[next]) printf("Forward Edge : (%d, %d)\n", cur, next);
        else if(finished[next] == 0) printf("Back Edge : (%d, %d)\n", cur, next);
        else printf("Cross Edge : (%d, %d)\n", cur, next);
    }
    finished[cur] = 1;
}