from collections import deque

def solution(board):
    n = len(board)
    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]
    visited = [[-1] * n for _ in range(n)]
    
    visited[0][0] = 0 # 시작점 초기화
    q = deque()
    q.append((0, 0, 0, 0))
    q.append((0, 0, 0, 1))
    while q:
        c, y, x, d = q.popleft()
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            # 범위 예외처리
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            # 벽인 경우
            if board[ny][nx] == 1:
                continue
            if k == d:
                cost = 100
            else:
                cost = 600
            
            nc = c + cost
            # 아직 방문하지 않은 곳이거나
            # 이미 방문했지만 현재 경로의 비용이 더 낮거나 같은 경우
            if visited[ny][nx] == -1 or nc <= visited[ny][nx]:
                visited[ny][nx] = nc
                q.append((nc, ny, nx, k))
    return visited[n-1][n-1]