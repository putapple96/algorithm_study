#include <bits/stdc++.h>
#define MAX_NUM 21
using namespace std;

int r, c;
char board[MAX_NUM][MAX_NUM];
int alphabetFlag[26] = {0,}; // A to Z : 1이면 현재 경로에 존재하는 알파벳

int dx[4] = {0, 0, -1, 1};
int dy[4] = {1, -1, 0, 0};
int ans = 1;

void dfs(int y, int x, int cnt){
    ans = max(ans, cnt);
    for(int i = 0; i < 4; i++){
        int ny = y + dy[i];
        int nx = x + dx[i];
        // out of range 예외 처리
        if(ny >= r || nx >= c || ny < 0 || nx < 0) continue;
        // 현재 알파벳 char 값을 int 형으로 변환.
        // 이 부분을 생각해 내는 것이 가장 중요
        int cur = (int)board[ny][nx] - 65; 
        if(alphabetFlag[cur]) continue;  
        //if(path.find(board[ny][nx]) != -1) continue; // 이미 지나온 길
        // ** string 의 find 사용시 시간초과 ** 
        alphabetFlag[cur]++;
        dfs(ny, nx, cnt + 1);
        alphabetFlag[cur]--;
        // path = path.substr(0, path.size() - 1);
    }
}
int main(){
    cin >> r >> c;
    for(int y = 0; y < r; y++){
        for(int x = 0; x < c; x++){
            cin >> board[y][x];
        }
    }
    //string pathString = "";
    //pathString += board[0][0];
    alphabetFlag[(int)board[0][0] - 65]++; // (0,0) visited
    dfs(0, 0, ans);
    cout << ans;
}