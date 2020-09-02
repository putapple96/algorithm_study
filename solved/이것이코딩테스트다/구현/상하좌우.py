
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

move = ['L', 'R', 'D', 'U']

n = int(input())
plans = input().split()

x = y = 1

for plan in plans:
    for k in range(len(move)):
        if plan == move[k]:
            ny = y + dy[k]
            nx = x + dx[k]

    if ny < 1 or nx < 1 or ny > n or nx > n:
         continue
    x = nx
    y = ny
  
               
print(x, y)
