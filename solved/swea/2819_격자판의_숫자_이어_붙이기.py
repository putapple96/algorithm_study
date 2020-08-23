
#dfs 와 set의 성질(중복된 원소 제거)을 이용하면 되는 문제

T = int(input())

dy = [-1, 1, 0 ,0]
dx = [0, 0, -1, 1]

def dfs(y, x, candi):
    if len(candi) == 7:
        numbers.add(candi)
        return
    
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if ny >= 0 and ny < 4 and nx >=0 and nx < 4:
            dfs(ny, nx, candi + board[ny][nx])


for i in range(T):
    board = []
    numbers = set()
    for _ in range(4):
        board.append(list(input().split()))
    for y in range(4):
        for x in range(4):
            dfs(y, x, board[y][x])
    print("#{} {}".format(i+1, len(numbers)))
    
    