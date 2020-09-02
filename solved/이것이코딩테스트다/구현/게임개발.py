dy = [-1, 0, 1, 0] # 북 서 남 동
dx = [0, -1, 0, 1]

n, m = map(int, input().split())

cur_y, cur_x, direction = map(int, input().split())
visited = [[False] * m for _ in range(n)]

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def rotate():
    global direction
    direction = (direction + 1) % 4

count = 1
turn_cnt = 0
visited[cur_y][cur_x] = True
while True:
    rotate()
    nx = cur_x + dx[direction]
    ny = cur_y + dy[direction]
    if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == False and board[ny][nx] == 0:
        visited[ny][nx] = True
        cur_x = nx
        cur_y = ny
        count += 1
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1

    if turn_cnt == 4: # 한칸 뒤로 돌아간다
        nx = cur_x - dx[direction]
        ny = cur_y - dy[direction]

        if nx < 0 or ny < 0 or nx >= m or ny >= n or board[ny][nx] == 1 or visited[ny][nx]:
            break
    
        turn_cnt = 0


print(count)


