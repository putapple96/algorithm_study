num = list(map(int, input()))


zero_cnt = 0 # 전체 0으로 바꿀 때 필요한 횟수
one_cnt = 0 # 전체 1으로 바꿀 때 필요한 횟수

if num[0] == 1:
    zero_cnt += 1
else:
    one_cnt += 1

for i in range(len(num) - 1):
    if num[i] != num[i+1]:
        if num[i+1] == 1:
            zero_cnt += 1
        else:
            one_cnt += 1

print(min(zero_cnt, one_cnt))