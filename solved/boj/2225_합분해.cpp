#include <iostream>
#include <cstring>
using namespace std;

int cache[201][201];

int n, k;

int solve(int sum, int toPick){
    if(sum > n) return 0;
    if(toPick == k){
        if(sum == n) return 1;
        else return 0;
    }

    int& ret = cache[sum][toPick];
    if(ret != -1) return ret;
    ret = 0;

    for(int i = 0; i <= n; i++){
        ret += solve(sum + i, toPick + 1);
        ret %= 1000000000;
    }
    return ret;
}

int main(){
    cin >> n >> k;
    memset(cache, -1, sizeof(cache));

    cout << solve(0,0);
    return 0;
}