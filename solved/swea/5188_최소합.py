from collections import deque

t = int(input())

dy = [1, 0]
dx = [0, 1]


def get_sum(y, x):
    global candi, ret
    if ret < candi:
        return
    if y == n-1 and x == n-1:
        ret = candi
        return

    for k in range(2):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny < 0 or nx < 0 or ny >=n or nx >=n or visited[ny][nx]:
            continue
        else:
            visited[ny][nx] = True
            candi += m[ny][nx]
            get_sum(ny, nx)
            visited[ny][nx] = False
            candi -= m[ny][nx]

for tc in range(t):
    n = int(input())
    m = [] # 숫자 적힌 판
    for _ in range(n):
        m.append(list(map(int, input().split())))
    visited = [[False] * n for _ in range(n)]
    candi = m[0][0]
    ret = 987654321
    get_sum(0,0)
    print("#{} {}".format(tc+1, ret))