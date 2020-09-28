def oper_R(arr):
    row = len(arr)
    col = len(arr[0])
    max_len = 0
    ret = [[] for _ in range(row)]
    for i in range(row):
        dic = {}
        for num in arr[i]:
            if num == 0:
                continue
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        res = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        if len(res) > 50:
            res = res[:50]
        max_len = max(max_len, len(res))
        for a, b in res:
            ret[i].append(a)
            ret[i].append(b)
    max_len *= 2
    for i in range(len(arr)):
        if len(ret[i]) < max_len:
            ret[i].extend([0] *(max_len - len(ret[i])))
    
    return ret
"""
def oper_C(arr):
    row = len(arr)
    col = len(arr[0])
    max_len = 0
    ret = [[] for _ in range(col)]
    for x in range(col):
        dic = {}
        for y in range(row):
            if arr[y][x] == 0:
                continue
            if arr[y][x] not in dic:
                dic[arr[y][x]] = 1
            else:
                dic[arr[y][x]] += 1
       
        res = sorted(dic.items(), key=lambda x: (x[1], x[0]))
        max_len = max(max_len, len(res))
        for a, b in res:
            ret[x].append(a)
            ret[x].append(b)
        

    max_len *= 2
    result = [[0] * col for _ in range(max_len)]
    
    for y in range(col):
        for i in range(len(ret[y])):
            result[i][y] = ret[y][i]
    #for i in range(max_len):
    #    print(result[i])

    return result

"""

def solve():
    r, c, k = map(int, input().split()) # row, column, target value
    r -= 1
    c -= 1
    arr = []
    for _ in range(3):
        arr.append(list(map(int, input().split())))
    t = 0
    if r < len(arr) and c < len(arr[0]):
        if arr[r][c] == k: return t

    while True:
        if len(arr) >= len(arr[0]):
            arr = oper_R(arr)
        else:
            arr = list(map(list, zip(*arr)))
            arr = oper_R(arr)
            arr = list(map(list, zip(*arr)))
        t += 1
        if t > 100: return -1
        if r < len(arr) and c < len(arr[0]):
            if arr[r][c] == k: return t
print(solve())