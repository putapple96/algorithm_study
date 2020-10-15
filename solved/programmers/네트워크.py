def dfs(start, com, visited):
    if not visited[start]:
        visited[start] = True
    
    for i in range(len(com)):
        if com[start][i] and not visited[i]:
            dfs(i, com, visited)

def solution(n, computers):
    ans = 0
    visited = [False] * n
    done = False
    while not done:
        done = True
        for i in range(n):
            if not visited[i]:
                done = False
                dfs(i, computers, visited)
                ans += 1
    
    return ans