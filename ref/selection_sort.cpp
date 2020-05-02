#include <bits/stdc++.h>
#define MAX_NUM 50
#define SWAP(x, y, temp) ( (temp)=(x), (x)=(y), (y)=(temp))
using namespace std;

int input[MAX_NUM];
int num;

void selectionSort(){
    int least, tmp;
    int i;
    // 맨 마지막 원소는 자동 정렬 되므로 num - 1 까지
    for(i = 0; i < num - 1; i++){ 
        least = i;
        // i+1 번째에서 배열의 끝까지의 범위에서 최솟값의 index를 찾아준다
        for(int j = i + 1; j < num; j++){
            if(input[j] < input[least])
                least = j;
        }
        if(i != least){ // 최소가 자기 자신이면 swap 할 필요 X
            swap(input[i], input[least]);
            //SWAP(input[i], input[least], tmp);
        }
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
    
    selectionSort();
    printf("\n\n=====Sorted Result====\n\n");
    for(int i = 0; i < num; i++)
        printf("%d ", input[i]);
}