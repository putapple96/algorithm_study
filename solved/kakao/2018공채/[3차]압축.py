def solution(msg):
    dic = dict()
    alpha = []
    [alpha.append(chr(i)) for i in range(ord('A'), ord('Z') + 1)]

    for idx, char in enumerate(alpha, 1):
        dic[char] = idx
    
    idx = 0
    max_index = 26
    length = 0
    answer = []
    while True:
        length += 1
        if not msg[idx:idx+length] in dic:
            answer.append(dic[msg[idx:idx+length - 1]])
            max_index += 1
            dic[msg[idx:idx+length]] = max_index
            idx += length - 1
            length = 0
        
        else:
            if idx + length - 1 == len(msg):
                answer.append(dic[msg[idx:idx+length - 1]])
                break
    
    return answer



