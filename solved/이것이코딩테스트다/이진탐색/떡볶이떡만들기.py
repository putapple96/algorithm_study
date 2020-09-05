def binary_search(arr, start, end):
    ret = -1
    while start <= end:
        remain_sum = 0
        mid = (start + end ) // 2
        for i in range(len(arr)):
            if mid < arr[i]:
                remain_sum += (arr[i] - mid)
        if remain_sum > m:
            start = mid + 1
        else:
            ret = mid
            end = mid - 1
    
    return ret

n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

print(binary_search(arr, 0, arr[-1]))

