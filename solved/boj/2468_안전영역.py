from copy import deepcopy
from collections import deque

n = int(input())

area = []

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

def solve(start, area):
    q = deque()
    q.append(start)

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if ny < 0 or nx < 0 or ny >=n or nx >= n:
                continue
            if area[ny][nx] != -1:
                area[ny][nx] = -1
                q.append((ny,nx))

for _ in range(n):
    area.append(list(map(int, input().split())))

ans = -1
highest = -1

for i in range(n):
    for j in range(n):
        highest = max(highest, area[i][j])


for h in range(highest):
    temp = []
    temp = deepcopy(area)
    for i in range(n):
        for j in range(n):
            if temp[i][j] <= h:
                temp[i][j] = -1

    candi = 0
    for i in range(n):
       for j in range(n):
           if temp[i][j] != -1:
               solve((i, j), temp)
               candi += 1
    ans = max(ans, candi)

print(ans)
