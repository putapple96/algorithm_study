from collections import deque


dy = [-1, 0, 1, 1, 1, 0, -1, -1]
dx = [1, 1, 1, 0, -1, -1, -1, 0]



def bfs(cur_pos, board):
    q = deque()
    q.append(cur_pos)
    while q:
        y, x = q.popleft()
        board[y][x] = 0
        for k in range(8):
            ny = y + dy[k]
            nx = x + dx[k]
            if ny < 0 or nx < 0 or ny >= h or nx >=w:
                continue
            if board[ny][nx] == 1:
                q.append((ny,nx))
                board[ny][nx] = 0
   
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0: break
    cnt = 0
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    for y in range(h):
        for x in range(w):
            if board[y][x] == 1:
                bfs((y,x), board)
                cnt += 1
    print(cnt)