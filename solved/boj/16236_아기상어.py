from collections import deque

n = int(input())

board = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(start, board):
    q = deque()
    q.append(start) # start = (아기상어 y, 상어x)
    dist = [[-1] * n for _ in range(n)] # 거리계산용. -1은 아직 방문하지 않았음을 의
    dist[start[0]][start[1]] = 0 # 현재 위치 거리값 초기화

    candi = []
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if ny < 0 or nx < 0 or ny >= n or nx >= n or dist[ny][nx] != -1:
                continue
            if board[ny][nx] > shark_size:
                continue
            
            if board[ny][nx] == 0:
                q.append((ny,nx))
                dist[ny][nx] = dist[y][x] + 1
            elif board[ny][nx] != 0 and board[ny][nx] <= shark_size:
                q.append((ny,nx))
                dist[ny][nx] = dist[y][x] + 1
                if board[ny][nx] < shark_size:
                    candi.append((dist[ny][nx], ny, nx))
    return candi

#문제에서 주어진 대로 초기값 설정
shark_size = 2 #아기 상어의 현재 크기
current_ate = 0 #아기 상어가 먹은 수
cur_y = 0 # 아기 상어의 y좌표
cur_x = 0 # 아기 상어의 x좌표
time = 0 # 경과한 시간

for _ in range(n):
    board.append(list(map(int, input().split())))


baby_q = deque()

for i in range(n):
    for j in range(n):
        if board[i][j] == 9: # 아기 상어 찾음
            # 현재 아기상어 좌표 업데이트 해주고 아기상어 큐에 넣어줌
            cur_y = i
            cur_x = j
            baby_q.append((cur_y, cur_x))
            board[i][j] = 0
            break
        
while baby_q:
    cur_y, cur_x = baby_q.popleft()
    # bfs를 해서 현재 위치의 아기상어가 먹을 수 있는 먹이의 후보군들을
    # (먹이까지 거리, 먹이의 y좌표, 먹이의 x좌표)의 튜플 형태의 리스트로 받아
    candidates = bfs((cur_y,cur_x), board)
    
    # 만약 candidates의 길이가 0이라면 더이상 움직일 수 없다는 것이므
    if(len(candidates) == 0):
        print(time) # 경과시간 출력후 break
        break
    else:
        sort_candi = sorted(candidates)
        cur_y = sort_candi[0][1] # 먹이가 존재하는 y좌표
        cur_x = sort_candi[0][2] # 먹이가 존재하는 x좌표
        time += sort_candi[0][0] # 그 먹이까지 가는데 걸리는 시간을 현재 시간에 더해줌
        board[cur_y][cur_x] = 0 # 먹었으니까 0으로 바꾸어줌
        current_ate += 1 # 현재 먹은 개수 1 증가
        baby_q.append((cur_y, cur_x)) # 아기상어의 좌표를 큐에 집어넣어줌
        if current_ate == shark_size: # 먹은 개수랑 상어 크기랑 같으면
            current_ate = 0 # 먹은개수 0으로 초기화하고
            shark_size += 1 # 사이즈 1증가 

