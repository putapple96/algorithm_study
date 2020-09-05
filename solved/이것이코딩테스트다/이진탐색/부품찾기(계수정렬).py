n = int(input())
arr = [0] * 1000000

for i in input().split():
    arr[int(i)] = 1

m = int(input())
b = list(map(int, input().split()))

for key in b:
    if arr[key] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')