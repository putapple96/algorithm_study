#include <iostream>
#include <algorithm>
#include <string>

using namespace std;
int n, m;
int board[1001][1001], dp[1001][1001];
string str;
int ans = 0;

int main(){
    cin >> n >> m;
    for(int i = 0; i < n ; i++){
        cin >> str;
        for(int j = 0; j < m; j++){
            board[i][j] = str[j] - 48;
            if(board[i][j] == 1){
                dp[i][j] = 1;
                ans = 1;
            }
        }
    }
    for(int y = 1; y < n; y++){
        for(int x = 1; x < m; x++){
            if(board[y-1][x] == 1 && board[y-1][x-1] == 1 && board[y][x-1] == 1){
                dp[y][x] = min(dp[y-1][x], dp[y-1][x-1]);
                dp[y][x] = min(dp[y][x], dp[y][x-1]) + 1; 
            }
            ans = max(ans, dp[y][x]);
        }
    }
    cout << ans * ans << endl;
}