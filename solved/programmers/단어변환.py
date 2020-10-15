from collections import deque

def bfs(start, target, words, visited):
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        if cur == target:
            break
        
        for word in words:
            diff = 0
            for s1, s2 in zip(word, cur):
                if s1 != s2:
                    diff += 1
            if diff == 1 and visited[word] == 0:
                visited[word] = visited[cur] + 1
                q.append(word)

def solution(begin, target, words):
    visited = {}
    visited[begin] = 0
    for word in words:
        visited[word] = 0
    bfs(begin, target, words, visited)
    try: return visited[target]
    except: return 0