loc = input()

x = int(loc[1])
y = int(ord(loc[0])) - 97 + 1

dy = [-2, -2, 2, 2, 1, -1, 1, -1]
dx = [-1, 1, 1, -1, 2, 2, -2, -2]

count = 0

for k in range(8):
    ny = y + dy[k]
    nx = x + dx[k]
    if ny < 1 or nx < 1 or nx > 8 or ny > 8:
        continue
    count += 1

print(count)    