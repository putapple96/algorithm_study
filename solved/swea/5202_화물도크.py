t = int(input())

for tc in range(t):
    n = int(input())

    dock_info = []
    for _ in range(n):
        s, e = map(int, input().split())
        dock_info.append((e, s))
    
    dock_info.sort()

    result = [dock_info[0]]

    j = 0
    for i in range(1, n):
        if dock_info[i][1] >= dock_info[j][0]:
            result.append(dock_info[i])
            j = i
    
    print("#{} {}".format(tc+1, len(result)))