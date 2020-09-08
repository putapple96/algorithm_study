"""
효율성 X. 정확성만 통과
"""
def solution(gems):
    kind_cnt = len(set(gems))
    min_interval = [0, 0]
    left = 0
    right  = 0
    min_length = 987654321
    while (left <= right and right < len(gems)):
        cur_gems = gems[left:right+1]
        cur_kind_cnt = len(set(cur_gems))
        cur_len = right - left + 1
        if cur_kind_cnt == kind_cnt:
            if cur_len < min_length:
                min_interval[0] = left + 1
                min_interval[1] = right + 1
                min_length = cur_len
            elif cur_len == min_length:
                if min_interval[0] > left:
                    min_interval[0] = left + 1
                    min_interval[1] = right + 1
                    min_length = cur_len
            left += 1
        else:
            right += 1
    return min_interval

