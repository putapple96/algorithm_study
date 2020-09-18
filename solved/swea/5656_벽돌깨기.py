from itertools import product
from copy import deepcopy

# 해당 열의 맨위 블록에 대해 조사
def bomb(b, col):
    for y in range(h):
        # 한개만 터지는 경우
        if b[y][col] == 1:
            b[y][col] = 0
            break
        # 여러개에 영향을 미치는 경우 +10을 해서 표시해준다.
        elif b[y][col] > 1:
            b[y][col] += 10
            break
    isDone = False
    while not isDone:
        isDone = bomb_process(b)
def bomb_process(b):
    isDone = True # 더 이상 폭발할 벽돌이 없다면 True
    for y in range(h):
        for x in range(w):
            # 여러개 영향 미치는 경우
            if b[y][x] > 10:
                num = b[y][x] - 10
                b[y][x] = 0 # 현재 위치 블럭 제거
                # 좌, 우 범위 설정. 보드의 범위를 나가지 않도록 max, min 이용
                left_x = max(0, x - num + 1) 
                right_x = min(w-1, x + num - 1)
                for nx in range(left_x, right_x+1):
                    # 1이라면 지워버리기
                    if b[y][nx] == 1: b[y][nx] = 0
                    # 그렇지 않다면 또 지워야 하므로 체크 해놓고 isDone을 False로
                    elif 1 < b[y][nx] < 10:
                        b[y][nx] += 10
                        isDone = False
                
                up_y = max(0, y - num + 1)
                down_y = min(h-1, y + num - 1)

                for ny in range(up_y, down_y + 1):
                    if b[ny][x] == 1: b[ny][x] = 0
                    elif 1 < b[ny][x] < 10:
                        b[ny][x] += 10
                        isDone = False
    return isDone

def down(b):
    for k in range(w):
        for j in range(h-1, -1, -1):
            # 빈 칸이 있다면
            if b[j][k] == 0:
                # 해당 빈칸의 위에
                for y in range(j-1, -1, -1):
                    # 폭발되지 않은 벽돌이 있다면
                    if b[y][k] != 0:
                        # 해당 벽돌을 아래로
                        b[j][k] = b[y][k]
                        b[y][k] = 0
                        break
# 남은 블럭 카운트
def block_count(b):
    cnt = 0
    for y in range(h):
        for x in range(w):
            if b[y][x] != 0:
                cnt +=1
    
    return cnt

t = int(input())
for tc in range(1, t+1):
    ans = 50
    n, w, h = map(int, input().split())
    board = []
    for _ in range(h):
        board.append(list(map(int, input().split())))
    
    select = [i for i in range(w)]
    candidates = list(product(select, repeat=n))
    for candi in candidates:
        tmp = deepcopy(board)
        for c in candi:
            bomb(tmp, c)
            down(tmp)
            ans = min(ans, block_count(tmp))
            
    print("#{} {}".format(tc, ans))

