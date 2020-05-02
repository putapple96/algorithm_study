#include <bits/stdc++.h>

#define MAX_NUM 50

using namespace std;
int input[MAX_NUM];
int num;

void quickSort(int first, int last){
    int pivot;
    int i, j;
    if(first < last){
        pivot = first;
        i = first;
        j = last;
        
        while(i < j){
            while(input[i] <= input[pivot] && i < last){
                i++;
            }
            while(input[j] > input[pivot]){
                j--;
            }
            if(i < j){
                swap(input[i], input[j]);
            }
        }
        swap(input[pivot], input[j]);

        quickSort(first, j - 1);
        quickSort(j + 1, last);
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
    
    quickSort(0, num - 1);
    printf("\n\n=====Sorted Result====\n\n");
    for(int i = 0; i < num; i++)
        printf("%d ", input[i]);
}