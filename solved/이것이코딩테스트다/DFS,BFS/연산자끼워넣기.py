# 백준 14888번
n = int(input())

num = list(map(int, input().split()))

add, sub, mul, div = map(int, input().split())

min_val = 987654321
max_val = -987654321

def solve(idx, cur_val):
    global min_val, max_val, add, sub, mul, div
    #print(cur_val)
    if idx == n:
        min_val = min(min_val, cur_val)
        max_val = max(max_val, cur_val)
    else:
        if add > 0:
            add -= 1
            solve(idx + 1, cur_val + num[idx])
            add += 1
        if sub > 0:
            sub -= 1
            solve(idx + 1, cur_val - num[idx])
            sub += 1
        if mul > 0:
            mul -= 1
            solve(idx + 1, cur_val * num[idx])
            mul += 1
        if div > 0:
            div -= 1
            solve(idx + 1, int(cur_val / num[idx]))
            div += 1


solve(1, num[0])
print(max_val)
print(min_val)
