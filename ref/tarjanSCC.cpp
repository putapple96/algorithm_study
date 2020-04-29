/*
    타잔의 강결합 컴포넌트 분리 알고리즘
*/
#include <bits/stdc++.h>

using namespace std;

// 인접리스트
vector<vector<int> > adj;
// 각 정점의 component 번호(0부터 시작)
// 같은 SCC 들끼리는 같은 번호를 갖는다
vector<int> sccId;
// 정점에 대한 탐색 순서 저장할 벡터
vector<int> visited;
// 정점 번호 저장할 스택
stack<int> s;

int sccCounter, vertextCounter;

// 현재 노드를 루트로 하는 서브트리들을 탐색하며
// 역방향 간선 또는 교차 간선을 통해 갈 수 있는 정점 중 
// 최소 발견 순서를 반환
// 이미 강결합으로 묶인 경우(sccId != -1)는 무시.
int scc(int cur){
    int ret = visited[cur] = vertextCounter++;
    // stack에 현재 노드를 넣는다.
    // stack에서 후손들은 현재 노드(cur) 이후에 들어감
    s.push(cur);
    for(int i = 0; i < adj[cur].size(); i++){
        int next = adj[cur][i];
        // 트리 간선일 때
        if(visited[next] == -1) ret = min(ret, scc(next)); 
        // 트리 간선(DFS spanning tree의 간선들) 은 아니지만 교차간선이 아닐 때
        else if(sccId[next] == -1) ret = min(ret, visited[next]); 
    }
    // cur 에서 부모 노드로 가는 간선을 끊어야 할지 결정한다
    if(ret == visited[cur]){
        // 현재 노드를 root로 하는 서브트리들에 남아있는 정점을 전부 하나의 결합으로 묶어준다.
        while(true){
            int top = s.top();
            s.pop();
            sccId[top] = sccCounter; // 같은 결합으로
            if(top == cur) break;
        }
        sccCounter++;
    }
    return ret;
}


vector<int> tarjanSCC(){
    // 배열 초기화
    sccId = visited = vector<int>(adj.size(), -1);
    // counter 초기화
    sccCounter = vertextCounter = 0;
    // 모든 정점에서 scc를 호출
    for(int i = 0; i < adj.size(); i++){
        if(visited[i] == -1) scc(i);
    }
    // 강결합한 결과 배열 sccId를 return 해줌
    return sccId;
}
