#include <bits/stdc++.h>

using namespace std;

int T;
int n, k;
int v[100], c[100];
int dp[101][1001]; // dp[총 가방 개수+1][최대 무게+1]
// dp[i][j] =  부피제한 j 에서 가방에 i번째 물건까지 넣었을 때 최대 가치

int main(){
    cin >> T;
    for(int tc = 1; tc <= T; tc++){
        cin >> n >> k;
        for(int i = 0; i < n; i++)
            cin >> v[i] >> c[i];
        for(int i = 0; i <=n; i++){
            for(int j = 0; j<=k; j++){
                if(i == 0 || j == 0)
                    dp[i][j] = 0; // 0개 뽑았거나 제한무게 0이면 가치 0   
                else if(v[i-1] <= j) // 가방크기인 j 보다 현재 물건의 부피가 작다면
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i-1]]+c[i-1]);    
                    // 현재 물건을 넣었을 때의 가치와 넣지 않았을 때의 가치 비교후 최대값 저장
                else  // 가방크기인 j 보다 현재 물건 부피가 크다면, i-1번째 물건까지 넣었을 때와 최대가치가 같다.
                    dp[i][j] = dp[i-1][j];
            }
        }
        printf("#%d %d\n", tc, dp[n][k]); // n개물건을 k의 부피 가방에 넣었을 때 최대값 : dp[n][k]
    }
}