#include <bits/stdc++.h>

using namespace std;

int tc;
int n, k; // 사람 수, 한번에 이동하는 칸의 수


void solve(int n, int k){
    list<int> people;
    for(int i = 1; i <=n; i++){
        people.push_back(i);
    }
    list<int>::iterator suicide = people.begin(); // 현재 1번 사람을 가리킴
    // 2명 살아남을 때 까지 반복
    while(n > 2){
        suicide = people.erase(suicide); // 현재 죽은 사람의 다음을 가리키게 됨.
        if(suicide == people.end()){ // 한바퀴 다 돌았으면 다시 처음으로
            suicide = people.begin();
        }
        n--;
        for(int i = 0; i < k - 1; i++){ // k-1 번 시계방향으로 옮긴다.
            suicide++;
            if(suicide == people.end()){ // 옮기는 와중에 한바퀴 돌면 다시 처음으로
               suicide = people.begin();
            }
        }
    }
    printf("%d %d\n", people.front(), people.back()); // 생존자 출력
}

int main(){
    cin >> tc;
    while(tc--){
        cin >> n >> k;
        solve(n, k);
    }
}