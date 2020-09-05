# 위상정렬

from collections import deque
from copy import deepcopy

n = int(input())

# 진입차수 0으로 초기화
indegree = [0] * (n + 1)

# 각 노드의 간선 정보를 저장 하기 위한 list
graph = [[] for _ in range(n + 1)]

# 강의 듣는데 필요한 시간 0으로 초기화
time = [0] * (n + 1)

for i in range(1, n + 1):
    info = list(map(int, input().split()))
    time[i] = info[0]
    for item in info[1:-1]:
        indegree[i] += 1
        graph[item].append(i)

def topology_sort():
    result = deepcopy(time)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            result[i] = max(result[i], result[cur] + time[i])
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1, n + 1):
        print(result[i])

topology_sort()