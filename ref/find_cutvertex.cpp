// 절단점 찾기
#include <bits/stdc++.h>

using namespace std;

vector<vector<int> > adj;
vector<int> order; // 발견순서. 초기값 -1

vector<bool> isCutVertex; // 절단점인지 여부

int counter = 0;
// current vertex를 루트로하는 서브트리


int findCutVertext(int cur, bool isRoot){
    order[cur] = counter++;
    int ret = order[cur];
    int child = 0;
    // cur Vertex를 루트로하는 서브트리들의 절단점을 찾기.
    for(int i = 0; i < adj[cur].size(); i++){
        int next = adj[cur][i];
        if(order[next] == -1){
            child++;
            // 해당 서브트리에서 갈수있는 가장 높은 정점 번호
            int subtree = findCutVertext(next, false);
            // 그 노드가 자기 자신 밑에있다면(자기보다 세대가 낮다면) 현재위치는 절단점이다
            if(!isRoot && subtree >= order[cur]){
                isCutVertex[cur] = true;
            }
            ret = min(ret, subtree);
        }
        else{
            ret = min(ret, order[next]);
        }
    }
    // 루트라면 서브트리개수가 1개 초과인 경우 부조건 절단점이된다.
    if(isRoot) isCutVertex[cur] = (child >= 2);
    return ret;
}

