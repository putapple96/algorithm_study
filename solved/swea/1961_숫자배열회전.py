# 시계 방향 90도 회전
def rotate_90(arr):
    n = len(arr)
    ret = [[0] * n for _ in range(n)]

    for y in range(n):
        for x in range(n):
            ret[x][n-y-1] = arr[y][x]
    return ret

t = int(input())

for tc in range(1, t + 1):
    print("#{}".format(tc))
    n = int(input())
    a = []
    rot = []
    for _ in range(n):
        a.append(list(map(str, input().split())))
    
    for _ in range(3):
        a = rotate_90(a)
        rot.append(a)
    
    for i in range(len(rot)):
        for j in range(len(rot)):
            print(''.join(rot[j][i]), end=' ')
        print()
