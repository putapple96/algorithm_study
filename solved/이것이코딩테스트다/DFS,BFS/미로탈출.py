from collections import deque

n, m = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

miro = []
dist = [[-1] * m for _ in range(n)]

for _ in range(n):
    miro.append(list(map(int, input())))

def bfs(y, x):
    q = deque()
    q.append((y,x))
    dist[y][x] = 0
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue
            if dist[ny][nx] != -1 or miro[ny][nx] == 0:
                continue

            dist[ny][nx] = dist[y][x] + 1
            q.append((ny, nx))
    
    return dist[n-1][m-1]

print(bfs(0,0))