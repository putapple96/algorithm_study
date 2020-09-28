from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, b):
    visited = [[-1] * w for _ in range(h)]
    visited[y][x] = 0
    q = deque()
    q.append((y,x))
    max_dist = -1
    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < h and 0 <= nx < w and visited[ny][nx] == -1\
                and b[ny][nx] == 'L':
                visited[ny][nx] = visited[y][x] + 1
                max_dist = max(max_dist, visited[ny][nx])
                q.append((ny, nx))
    
    return max_dist

h, w = map(int, input().split())

board = []
ans = -1
for _ in range(h):
    board.append(list(input()))

for y in range(h):
    for x in range(w):
        if board[y][x] == 'L':
            ans = max(ans, bfs(y, x, board))

print(ans)

