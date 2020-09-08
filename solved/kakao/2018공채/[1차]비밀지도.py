def solution(n, arr1, arr2):
    ans = []

    for first, second in zip(arr1, arr2):
        temp = str(bin(first | second))[2:]
        temp = '0' * (n - len(temp)) + temp
        temp = temp.replace('1', "#")
        temp = temp.replace('0', " ")
        ans.append(temp)
    return ans
    