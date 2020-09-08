def solution(N, stages):
    fail_rate = {}
    user_cnt = len(stages)
    for i in range(1, N+1):
        if user_cnt == 0:
            fail_rate[i] = 0
            continue
        cur_user_cnt = stages.count(i)
        fail_rate[i] = stages.count(i) / user_cnt
        user_cnt -= cur_user_cnt
    
    answer = sorted(fail_rate, key= lambda x: fail_rate[x], reverse=True)

    return answer
