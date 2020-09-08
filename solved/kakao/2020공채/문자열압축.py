def solution(s):
    candi = []
    if len(s) == 1:
        return 1
    for i in range(1, len(s)): # 1개부터 길이까지 slice
        answer = ''
        count = 1
        for j in range(i, len(s), i):
            cur_str = s[j-i:j]
            next_str = s[j:j+i]
            if cur_str == next_str:
                count += 1
            else:
                if count == 1:
                    answer += cur_str
                else:
                    answer += str(count)+cur_str
                    count = 1
        if len(s[j:j+i]) == i: # next_str 이 slice 길이를 만족하면,
            if count == 1:
                answer += cur_str
            else:
                answer += str(count)+cur_str
                count = 1
        else:
            answer+=s[j:j+i]
        candi.append(len(answer))
    answer = min(candi)
    return answer