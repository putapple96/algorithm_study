n = int(input())

fear = list(map(int, input().split()))

fear.sort()

ret = 0
group_cnt = 0
for f in fear:
    group_cnt += 1
    if group_cnt >= f:
        ret += 1
        group_cnt = 0

print(ret)