n, m = map(int, input().split())

ice = []

for _ in range(n):
    ice.append(list(map(int, input())))

visited = [[False] * m for _ in range(n)]

def dfs(y, x):
    if y < 0 or x < 0 or y >= n or x >= m or visited[y][x]:
        return False
    
    if not visited[y][x] and ice[y][x] == 0:
        visited[y][x] = True
        dfs(y - 1, x)
        dfs(y + 1, x)
        dfs(y, x - 1)
        dfs(y, x + 1)
        return True
    return False

cnt = 0
for y in range(n):
    for x in range(m):
        if dfs(y, x):
            cnt += 1

print(cnt)
