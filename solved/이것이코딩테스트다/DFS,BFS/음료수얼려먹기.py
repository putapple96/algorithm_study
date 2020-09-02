from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

n, m = map(int, input().split())

ice = []

visited = [[False]*m for _ in range(n)]

def bfs(pos, ice):
    q = deque()
    q.append(pos)

    while q:
        y, x = q.popleft()
        visited[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            # 범위 밖인 경우에 대한 예외처리
            if ny < 0 or nx < 0 or nx >= m or ny >= n:
                continue
            # 이미 방문했거나, 칸막이가 존재한다면,
            if ice[ny][nx] == 1 or visited[ny][nx]:
                continue

            visited[ny][nx] = True
            q.append((ny,nx))
    



for _ in range(n):
    ice.append(list(map(int, input())))

cnt = 0
for y in range(n):
    for x in range(m):
        if ice[y][x] == 0 and not visited[y][x]:
            bfs((y, x), ice)
            cnt += 1

print(cnt)