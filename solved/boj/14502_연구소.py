from collections import deque
import copy

ret = 0
def bfs():
    global ret
    
    q = deque()
    board_temp = []
    #for i in range(n):
    #    board_temp.append(board[i])
    #print(board_temp)
    board_temp = copy.deepcopy(board)
    visited = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board_temp[i][j] == 2: # 현재 위치에 유해가스가 있다면,
                q.append([i, j])
                visited[i][j]= 1

    while q:
        cur_y, cur_x = q.popleft()

        for k in range(4):
            ny = cur_y + dy[k]
            nx = cur_x + dx[k]

            if(ny < 0 or ny >= n or nx < 0 or nx >= m):
                continue
            # 방문하지 않았고, 벽이 아니면,
            if visited[ny][nx] == 0 and board_temp[ny][nx] == 0:
                # 유해가스를 전파시키고, 방문했음을 표시후 큐에 넣어준다.
                board_temp[ny][nx] = 2
                visited[ny][nx] = 1
                q.append([ny, nx])
    ans = 0
    for i in range(n):
        for j in range(m):
            if board_temp[i][j] == 0: # 유해가스 퍼지지 않은 곳
                ans += 1


    if ret < ans:
        ret = ans


def pick(cnt, sy, sx):
    if cnt == 3:
        bfs()
        
        return
    for y in range(sy, n):
        for x in range(sx, m):
            if board[y][x] == 0:
                board[y][x] = 1
                
                pick(cnt+1, y, x)
                board[y][x] = 0
        sx = 0


n, m = map(int, input().split())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

pick(0, 0, 0)

print(ret)

