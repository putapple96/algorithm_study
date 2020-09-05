from itertools import combinations
n = int(input())
board = []
teacher = []
empty = []
for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teacher.append((i, j))
        elif board[i][j] == 'X':
            empty.append((i, j))
        
# y, x 위치에서 direction 방향에 있는 학생을 발견할 수 있는지 확인하는 함수
# direction 0 1 2 3 = 동 서 남 북
def check(y, x, direction):
    if direction == 0:
        while x < n:
            # 학생 발견
            if board[y][x] == 'S':
                return True
            # 장애물 발견
            elif board[y][x] == 'O':
                return False
            x += 1
    elif direction == 1:
       while x >= 0:
            # 학생 발견
            if board[y][x] == 'S':
                return True
            # 장애물 발견
            elif board[y][x] == 'O':
                return False
            x -= 1
    elif direction == 2:
        while y < n:
            # 학생 발견
            if board[y][x] == 'S':
                return True
            # 장애물 발견
            elif board[y][x] == 'O':
                return False
            y += 1
    elif direction == 3:
        while y >= 0:
            # 학생 발견
            if board[y][x] == 'S':
                return True
            # 장애물 발견
            elif board[y][x] == 'O':
                return False
            y -= 1
    
candis = list

def detect():
    for y, x in teacher:
        for i in range(4):
            if check(y, x, i):
                return True
    
    return False

def solve():
    for candi in combinations(empty, 3):
        for y, x in candi:
            board[y][x] = 'O'
        if not detect():
            print("YES")
            return
        for y, x in candi:
            board[y][x] = 'X'
    
    print("NO")
    return

solve()