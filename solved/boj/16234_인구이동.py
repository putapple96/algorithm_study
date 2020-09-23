from collections import deque

n, l, r = map(int, input().split())

b = []
for _ in range(n):
    b.append(list(map(int, input().split())))

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(y, x, b):
    q = deque()
    q.append((y, x))
    union = []
    pop_sum = b[y][x]
    visited[y][x] = True
    union.append((y, x))
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            
            if 0 <= ny < n and 0 <= nx < n and visited[ny][nx] == False and (l <= abs(b[ny][nx] - b[y][x]) <= r):
                visited[ny][nx] = True
                q.append((ny, nx))
                union.append((ny, nx))
                pop_sum += b[ny][nx]
    
    num = len(union)
    # 연합이 생성 안됐으므로 인구 이동 X
    if num == 1:
        return 0
    for y, x in union:
        b[y][x] = int(pop_sum / num)    
    return 1
    
move_cnt = 0
while True:
    union_cnt = 0
    visited = [[False] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                union_cnt += bfs(y, x, b)
    if union_cnt >= 1:
        move_cnt += 1
    else:
        break
print(move_cnt)
