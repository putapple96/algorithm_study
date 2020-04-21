#include <stdio.h>
#include <algorithm>

using namespace std;

int n;
int t[15], p[15];
int cache[15];


int solve(int day){
    if(day > n) return -987654321;
    if(day == n) return 0;

    int& ret = cache[day];
    if(ret != -1) return ret;
    ret = max(solve(day+1), solve(day+t[day])+p[day]);
    return ret;
}

int main(){
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        scanf("%d %d", &t[i], &p[i]);
        cache[i] = -1;
    }

    printf("%d\n", solve(0));
}