# head. number, tail로 나누는 함수
def seperate(s):
    head = ""
    number = ""
    tail = ""
    for i in range(len(s)):
        if not s[i].isnumeric(): head += s[i]
        elif s[i].isnumeric(): break
    for j in range(i, len(s)):
        if s[j].isnumeric(): number += s[j]
        else:
            tail = s[j:]
            break
    return head, number, tail
        
def solution(files):
    all_file = []
    for f in files:
        h, n, t = seperate(f)
        all_file.append([h, n, t])
   
    all_file.sort(key=lambda x: (x[0].lower(), int(x[1])))
    answer = []
    for h, n, t in all_file:
        answer.append(h + n + t)
    return answer