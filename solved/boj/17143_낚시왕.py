dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

R, C, M = map(int, input().split())

shark = []

board = [[[] for _ in range(C)] for _ in range(R)]

def move(r, c, s, d):
    tmp = s
    while tmp > 0:
        nr, nc = r + dr[d], c + dc[d]
        tmp -= 1
        if nr >= R:
            d = 0; nr -= 2
        elif nr < 0:
            d = 1; nr += 2
        elif nc >= C:
            d = 3; nc -= 2
        elif nc < 0:
            nc += 2; d = 2
        r = nr; c = nc
    return r, c, d

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    r -= 1; c -= 1; d -= 1
    board[r][c] = [s, d, z]


# 물고기를 낚는 함수
def catch(col):
    size = 0
    global M
    for y in range(R):
        if len(board[y][col]) != 0:
            size += board[y][col][2]
            board[y][col] = []
            M -=1
            break
    return size

idx = 0
ans = 0
while idx < C:
    ans += catch(idx)
    # 존재하는 상어를 다 잡았다면
    if M == 0:
        break
    idx += 1
    new_shark = [[[] for _ in range(C)] for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if len(board[y][x]) != 0:
                r = y
                c = x
                s, d, z = board[y][x][0], board[y][x][1], board[y][x][2]
                board[y][x] = []
                if d == 0 or d == 1:
                    T = 2 * R
                    r, c, d = move(r, c, s, d)
                elif d == 2 or d == 3:
                    T = 2 * C
                    r, c, d = move(r, c, s, d)
                if len(new_shark[r][c]) == 0:
                    new_shark[r][c] = [s, d, z]
                else:
                    if new_shark[r][c][2] < z:
                        new_shark[r][c] = [s, d, z]
                        M -= 1
    board = new_shark

print(ans)