n, k = map(int, input().split())

item = list(map(int, input().split()))
multi_tap = []
cnt = 0
for i in range(k):
    if item[i] in multi_tap:
        continue
    if len(multi_tap) == n:
        tap_max_idx, item_max_idx = 0, 0
        for j in range(len(multi_tap)):
            item_idx = 10e9
            for l in range(i+1, k):
                if multi_tap[j] == item[l]:
                    item_idx = l
                    break
            if item_max_idx < item_idx:
                item_max_idx = item_idx
                tap_max_idx = j
        
        multi_tap[tap_max_idx] = item[i]
        cnt += 1
    else:
        multi_tap.append(item[i])


print(cnt)
                    
