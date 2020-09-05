# 백준 18352번
from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

dist = [-1] * (n + 1)
dist[x] = 0 # 출발 도시 거리는 0
q = deque()
q.append(x)
while q:
    cur_node = q.popleft()

    for next_node in graph[cur_node]:
        if dist[next_node] == -1: # 아직 방문하지 않았다면,
            dist[next_node] = dist[cur_node] + 1
            q.append(next_node)
cnt = 0
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        cnt += 1

if cnt == 0:
    print(-1)
