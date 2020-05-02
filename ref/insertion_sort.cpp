#include <bits/stdc++.h>
#define MAX_NUM 50
using namespace std;

int input[MAX_NUM];
int num;

void insertionSort(){
    int key;
    int j;
    for(int i = 1; i < num; i++){
        key = input[i]; // key 값(삽입하고자 하는 값)
        j = i - 1; // key 왼쪽 부분에 대해 역순으로 탐색
        while((j >= 0) && (key < input[j])){
            // key가 정렬된 배열의 값보다 더 작고 j 가 음수가 아닌 경우,
            // j번째 값들을 오른쪽으로 한 칸씩 밀어준다.
            input[j + 1] = input[j];
            j--;
        }
        input[j + 1] = key;
    }
}

int main(){

    num = 50;
    srand((unsigned int)time(NULL));
    for(int i = 0; i < num; i++) 
        input[i] = rand() % 300;
    printf("=====Random Input====\n\n");
    for(int i = 0; i < num; i++) 
        printf("%d ", input[i]);
    
    insertionSort();
    printf("\n\n=====Sorted Result====\n\n");
    for(int i = 0; i < num; i++)
        printf("%d ", input[i]);
}