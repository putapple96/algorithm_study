import sys

input = sys.stdin.readline

r, c, t = map(int ,input().split()) # row, col, target time

board = []

for _ in range(r):
    board.append(list(map(int, input().split())))


def spread():
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    result = [[0] * c for _ in range(r)]
    
    for y in range(r):
        for x in range(c):
            # 먼지가 존재하는 곳
            if board[y][x] > 0:
               
                # 상하좌우 몇가지의 방향에 확산되었는지 count
                cnt = 0
                # 확산되는 양
                amount = int(board[y][x] / 5)
                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    # 확산하고자 하는 칸이 맵의 범위 내에 있고 벽이 아니라면,
                    if 0 <= ny < r and 0 <= nx < c and board[ny][nx] >= 0:
                        cnt += 1
                        result[ny][nx] += amount
                result[y][x] += (board[y][x] - amount * cnt)
                # 확산 완료되었으므로 0으로 바꾸어 준다.
                #board[y][x] = 0
    
   
    for y in range(r):
        for x in range(c):
            if board[y][x] == -1:
                continue
            else:
                board[y][x] = result[y][x]
    
   

# 공기 청정기 작동하는 함수
def clean():
    # 공기 청정기 위치
    up, down = -1, -1
    for y in range(r):
        if board[y][0] == -1:
            if up == -1:
                up = y
            else:
                down = y

    for x in range(up-2, -1, -1):
        
        board[x+1][0] = board[x][0]
    for x in range(c-1):
        board[0][x] = board[0][x+1]
    for x in range(up):
        board[x][c-1] = board[x+1][c-1]
    for x in range(c-2, -1, -1):
        board[up][x+1] = board[up][x]
    
    board[up][1] = 0

    for x in range(down+1, r-1):
        board[x][0] = board[x+1][0]
    for x in range(c-1):
        board[r-1][x] = board[r-1][x+1]
    for x in range(r-2, down-1, -1):
        board[x+1][c-1] = board[x][c-1]
    for x in range(c-2, -1, -1):
        board[down][x+1] = board[down][x]
    
    board[down][1] = 0

for _ in range(t):
    spread()
    clean()

ans = 2 # 공기청정기가 board 상에 -1 값을 가지므로
for y in range(r):
    for x in range(c):
        ans += board[y][x]

print(ans)