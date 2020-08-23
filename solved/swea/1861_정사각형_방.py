from collections import deque

dy = [-1 , 1, 0, 0]
dx = [0, 0, -1, 1]

tc = int(input())

def solve(s, room):
    q = deque()
    q.append(s)
    ret = 1
    room_num = room[s[0]][s[1]]

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if(ny < 0 or nx < 0 or ny >= n or nx >= n):
                continue
            if room[ny][nx] == room[y][x] +1:
                ret += 1
                q.append((ny, nx))
    return ret, room_num
        


for test_case in range(tc):
    n = int(input())
    rooms = []
    max_ans = -1
    min_room_num = 987654321 
    for _ in range(n):
        rooms.append(list(map(int, input().split())))
    for y in range(n):
        for x in range(n):
            ans, room_num = solve((y,x), rooms)
            if max_ans == ans:
                min_room_num = min(min_room_num, room_num)
            elif ans > max_ans:
                max_ans = ans
                min_room_num = room_num
    
    print("#{} {} {}".format(test_case+1, min_room_num, max_ans))
