#include <bits/stdc++.h>

using namespace std;

int tc;
string str;


bool isMatched2(const string& formula){
    const string opening("({["), closing(")}]"); 
    // 여는 괄호와 닫는 괄호 목록을 문자열에 저장. 서로 짝이 맞는 순서로 초기화해줘야한다.
    stack<char> openStack; // 여는 괄호 넣을 stack
    for(int i = 0; i < formula.size(); i++){
        // 여는 괄호인지 닫는 괄호인지 find 로 확인. 
        // find는 찾는 값이 문자열에 없다면 -1 을 리턴한다
        if(opening.find(formula[i]) != -1)
            openStack.push(formula[i]); // 여는 괄호이면 push
        else{
            // 스택이 비어있다면(짝이 안맞는다) false
            if(openStack.empty()) return false;
            // 서로 짝이 안맞는 경우
            if(opening.find(openStack.top()) != closing.find(formula[i]))
                return false;
            // 짝이 맞는 경우엔 pop
            openStack.pop();
        }
    }
    // 위의 과정을 다 거쳐도 스택이 비어있지않다면 짝이 안맞는 것임
    return openStack.empty();
}


bool isMatched(const string& bk){
    stack<char> s;
    for(int i = 0; i < bk.size(); i++){
        if(bk[i] == '(' || bk[i] == '{' || bk[i] == '['){
            s.push(bk[i]);
        }
        else{
            if(s.empty()) return false;
            if(bk[i] == ')' && s.top() != '(') return false;
            else if(bk[i] == '}' && s.top() != '{') return false;
            else if(bk[i] == ']' && s.top() != '[') return false;
            else{
                s.pop();
            }
        }
    }
    return s.empty();
}

int main(){
    cin >> tc;
    while(tc--){
        cin >> str;
        isMatched(str) ? printf("YES\n") : printf("NO\n");
    }
}