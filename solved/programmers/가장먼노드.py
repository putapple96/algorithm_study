from collections import deque

def solution(n, edge):
    visited = {(i+1):-1 for i in range(n)}
    node = {(i+1):[] for i in range(n)}
    for e in edge:
        a, b = e
        node[a].append(b)
        node[b].append(a)
 
    return bfs(1, visited, node)

def bfs(start, visited, node):
    q = deque()
    q.append(start)
    visited[start] = 0
    while q:
        cur = q.popleft()
        connected = node[cur]
        for n in connected:

            if visited[n] == -1:
                q.append(n)
                visited[n] = visited[cur] + 1
    
    ans = list(visited.values())
    return ans.count(max(ans))