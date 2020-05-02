#include <bits/stdc++.h>

using namespace std;

#define MAX_SIZE 100
int N, arr[MAX_SIZE]; 
int *arr2; // extra space

void merge(int left, int right){
    int mid = (left + right) / 2;
    int i = left;
    int j = mid + 1;
    int k = left;
    while(i <= mid && j <= right){
        if(arr[i] <= arr[j])
            arr2[k++] = arr[i++];
        else
            arr2[k++] = arr[j++];
    }
    int temp = i > mid ? j : i;

    while(k <= right) arr2[k++] = arr[temp++];

    for(int i = left; i <= right; i++) arr[i] = arr2[i];
}

void partition(int left, int right){
    int mid;
    if(left < right){
        mid = (left + right) / 2;
        partition(left, mid);
        partition(mid+1, right);
        merge(left, right);
    }
}

int main(){
    N = 50;
    arr2 = new int[N];
    srand((unsigned int)time(NULL));
    for(int i = 0; i < N; i++) 
        arr[i] = rand() % 300;
    printf("=====Random Input====\n\n");
    for(int i = 0; i < N; i++) 
        printf("%d ", arr[i]);
    
    partition(0, N - 1);
    printf("\n\n=====Sorted Result====\n\n");
    for(int i = 0; i < N; i++)
        printf("%d ", arr[i]);
}