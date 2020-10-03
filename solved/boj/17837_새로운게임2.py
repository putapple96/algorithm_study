n, k = map(int, input().split()) # 체스판 크기, 말으 ㅣ개수

dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

# 0 = 흰색, 1 = 빨강, 2 = 파랑
color_info = []
board = [[[] for _ in range(n)] for _ in range(n)]
horse = [[] for _ in range(k)]
for _ in range(n):
    color_info.append(list(map(int, input().split())))

for i in range(k):
    # 행, 열, 이동 방향
    r, c, d = map(int, input().split())
    #print(r, c)
    board[r-1][c-1].append(i)
    horse[i] = [r-1, c-1, d- 1]

# 방향 반대로 바꾸기
def d_change(d):
    if d == 0 or d == 2: return d + 1
    else: return d - 1

# 한 턴
def move(horse):
    for i in range(k):
        y, x, d = horse[i]
        ny = y + dy[d]
        nx = x + dx[d]
        # 체스판을 벗어나는 경우이거나 
        # 이동하려는 칸이 파랑칸이라면
        if ny < 0 or ny >=n or nx < 0 or nx >= n\
             or color_info[ny][nx] == 2:
            d = d_change(d) # 방향 바꾸고
            ny = y + dy[d]
            nx = x + dx[d]

            if ny < 0 or ny >=n or nx < 0 or nx >= n\
             or color_info[ny][nx] == 2:
                #horse[i][2] = d
                nx = x
                ny = y
                #continue
        horse[i] = [ny, nx, d]
        if nx == x and ny == y: continue
        tmp = []
        for idx, key in enumerate(board[y][x]):
            if key == i:
                # 현재 말 위의 것들을 tmp에 넣는다
                tmp = board[y][x][idx:]
                # 현재 말 밑에 있는 말만 남긴다
                board[y][x] = board[y][x][:idx]
                break
        
        # 이동할 위치가 빨강이라면
        if color_info[ny][nx] == 1:
            tmp = reversed(tmp)
        
        for h in tmp:
            board[ny][nx].append(h)
            # 말 정보 업데이트
            horse[h][:2] = [ny, nx]
        
        # 한 칸에 말이 4개 이상이라면 
        if len(board[ny][nx]) >= 4:
            # 게임이 끝남
            return False
    # 성공적으로 턴 종료
    return True


def solve():
    turn = 1
    while turn <= 1000:
        if move(horse): turn += 1
        else: return turn
    return -1

print(solve())