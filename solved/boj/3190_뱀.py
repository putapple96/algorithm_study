from collections import deque
dy = [0, 1, 0, -1] # 오, 아래, 왼, 위
dx = [1, 0, -1, 0]
d = 0 # 뱀 방향
t = 1 # 시간
def rotate(rot, d):
    if rot == 'L':
        return (d - 1) % 4
    else:
        return (d+1) % 4

n = int(input()) # 보드의 크기
board = [[0] * n for _ in range(n)]
k = int(input()) # 사과 개수

snake = deque()
snake.append((0, 0))
#snake.append((0, 1)) # 뱀의 꼬리, 머리 위치
for _ in range(k):
    y, x = map(int, input().split())
    board[y-1][x-1] = 2 # 사과 있는 위치 2로 표시

l = int(input())
# 뱀의 방향 전환 정보
dir_info = deque()
for _ in range(l):
    time, direction = input().split()
    dir_info.append([int(time), direction])

def move():
    global d # 방향, 시간
    # 뱀의 머리 위치
    hy = snake[-1][0]
    hx = snake[-1][1]
    ny = hy + dy[d]
    nx = hx + dx[d]
    # 범위 내에서 움직일 때
    if 0 <= ny < n and 0 <= nx < n:
        if (ny, nx) in snake:
            # 몸과 충돌하므로 False 리턴
            return False
        if board[ny][nx] == 2:
            # 꼬리 그대로, 머리만 append
            board[ny][nx] = 0
            snake.append((ny, nx))
        elif board[ny][nx] == 0:
            # 머리 위치 변경
            snake.append((ny, nx))
            snake.popleft() # 꼬리 한칸 줄임
    else:
        # 범위 벗어남
        return False
    return True

while True:
    check = move()
    if not check:
        break
    else:
        if dir_info:
            if t == dir_info[0][0]:
                d = rotate(dir_info[0][1], d)
                dir_info.popleft()
        t += 1
print(t)