from collections import deque


def bfs(v, pic, color):
    q = deque()
    q.append(v)

    while q:
        y, x = q.popleft()

        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]

            if(ny < 0 or nx < 0 or ny >=n or nx >=n):
                continue
            #아직 방문하지 않은 점이고, 같은 색상이면
            if(pic[ny][nx] != 'X' and pic[ny][nx] == color):
                #큐에 현재 위치 넣고
                q.append((ny,nx))
                # 이동했다는 표시(X)
                pic[ny][nx] = 'X'


n = int(input())

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

pic1 = [] #정상
pic2 = [[''] * n for _ in range(n)] #적록색약

for _ in range(n):
    pic1.append(list(input()))
for i in range(n):
    for j in range(n):
        if pic1[i][j] == 'G':
            pic2[i][j] = 'R'
        else:
            pic2[i][j] = pic1[i][j]

ans1 = ans2 = 0
for i in range(n):
    for j in range(n):
        if pic1[i][j] != 'X':
            bfs((i,j), pic1, pic1[i][j])
            ans1 += 1
            
for i in range(n):
    for j in range(n):
        if pic2[i][j] != 'X':
            bfs((i,j), pic2, pic2[i][j])
            ans2 += 1

print(ans1, ans2)
