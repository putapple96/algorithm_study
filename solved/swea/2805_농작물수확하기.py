def calc(arr):
    n = len(arr)
    mid = n // 2
    left = mid
    ret = 0
    # 마름모 윗부분
    for y in range(mid):
        for x in range(left, mid+y+1):
            ret += arr[y][x]
        left -= 1

    # 마름모 가운데
    ret += sum(arr[mid])
    left = 1

    # 마름모 아랫부분
    for y in range(mid+1, n):
        for x in range(left, n-left):
            ret += arr[y][x]
        left += 1
    return ret

t = int(input())


for tc in range(1, t + 1):
    farm = []
    n = int(input())
    for _ in range(n):
        farm.append(list(map(int, input())))
    print("#{} {}".format(tc, calc(farm)))
