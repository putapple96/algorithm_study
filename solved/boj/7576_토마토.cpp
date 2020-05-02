#include <bits/stdc++.h>
#define MAX_SIZE 1001
using namespace std;

queue<pair<int, int>> q; // 익은 토마토 저장할 큐

int m,n;
int board[MAX_SIZE][MAX_SIZE];

int ans = 0;

int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, 1, -1};


void bfs(){
    while(!q.empty()){
        int curY = q.front().first; // 현재 Y 좌표
        int curX = q.front().second; // 현재 X 좌표  
        q.pop();
        int ny, nx;
        for(int i = 0; i < 4; i++){
            ny = curY + dy[i];
            nx = curX + dx[i];
            // 범위 벗어나는 경우 예외처리
            if(ny >= n || nx >= m || ny < 0 || nx < 0) continue; 
            if(board[ny][nx] == 0){
                board[ny][nx] = board[curY][curX] + 1;
                q.push(make_pair(ny, nx));
            }
        }
    }
}

int main(){
    cin >> m >> n;
    for(int y = 0; y < n; y++){
        for(int x = 0; x < m; x++){
            cin >> board[y][x];
            // 익은 토마토의 위치를 기억해놓는다
            if(board[y][x] == 1){
               q.push(make_pair(y, x)); 
            } 
        }
    }
    bfs(); // bfs 탐색
    for(int y = 0; y < n; y++){
        for(int x = 0; x < m; x++){
            if(board[y][x] == 0) {
                cout << "-1\n";
                return 0;
            }
            if(ans < board[y][x]) ans = board[y][x]; // 그래프 내에 최대값(걸린 시간) 찾기
        }
    }
    cout << ans - 1 << endl;
}