from collections import deque


dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(v, board):
    q = deque()
    q.append(v)

    num = 0
    
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if(ny < 0 or nx < 0 or ny >=n or nx >=n):
                continue

            if board[ny][nx] == 1:
                num += 1
                board[ny][nx] = 0
                q.append((ny,nx))
    return num

n = int(input())

board = []
for _ in range(n):
    board.append(list(map(int, input())))


ans = []
for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            ans.append(dfs((y,x), board))



print(len(ans))
for number in sorted(ans):
    print(number)
