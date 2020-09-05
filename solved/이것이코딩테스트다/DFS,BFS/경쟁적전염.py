# 백준 18405번
from collections import deque
n, k = map(int, input().split())

board = []
q = []

for y in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for x in range(n):
        if data[x] != 0:
            q.append((data[x], 0, y, x))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

q.sort()
dq = deque(q)


target_time, target_y, target_x = map(int, input().split())


while dq:
    num, time, y, x = dq.popleft()
    if time == target_time:
        break
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        # 범위 체크
        if ny < 0 or nx < 0 or ny >=n or nx >= n:
            continue
        if board[ny][nx] == 0:
            board[ny][nx] = num
            dq.append((num, time + 1, ny, nx))
    
    
print(board[target_y - 1][target_x - 1])
