#include <bits/stdc++.h>

using namespace std;

int tc; // test case
int n; // # of phone number



void solve(const vector<string>& v){
    for(int i = 0; i < n - 1; i++){
        int curLen = v[i].length(); // 현재 문자열 길이
        // 현재 문자열이 그 다음 문자열의 접두사라면 NO
        if(v[i] == v[i+1].substr(0, curLen)){ 
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
    return;
}

int main(){
    cin >> tc;
    while(tc--){
        vector<string> v;
        cin >> n;
        for(int i = 0; i < n; i++){
            string tmp;
            cin >> tmp;
            v.push_back(tmp);
        }
        // 사전순으로 정렬해주는 순간 현재 문자열과 그 다음 문자열만 비교해주면 된다.
        sort(v.begin(), v.end()); 
        solve(v);
    }
}