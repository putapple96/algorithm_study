num = list(map(int, input()))

num.sort(reverse=True)

result = num[0]

for i in range(1, len(num)):
    if num[i] == 0:
        result += num[i]
    else:
        result *= num[i]

print(result)