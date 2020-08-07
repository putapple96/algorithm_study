from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(v, board):
    q = deque()
    q.append(v)
    while q:
        y, x = q.popleft()

        board[y][x] = 0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = 0
                q.append((ny, nx))

    return 1

tc = int(input())

for _ in range(tc):
    ans = 0
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    for c in range(m):
        for r in range(n):
            if board[r][c] == 1:
                dfs((r, c), board)
                ans += 1

    print(ans)
