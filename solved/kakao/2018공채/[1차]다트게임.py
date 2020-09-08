import re

def solution(dartResult):
    reg = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    info = reg.findall(dartResult)
    result = []
    for idx, cur in enumerate(info):
        score = cur[0]
        bonus = cur[1]
        option = cur[2]
        if bonus == 'S': bonus = 1
        elif bonus == 'D': bonus = 2
        elif bonus == 'T': bonus = 3

        if option == '*' :
            if idx == 0:
                result.append(int(score) ** bonus * 2)
            else:
                result[-1] *= 2
                result.append(int(score) ** bonus * 2)
        elif option == '#':
            result.append(int(score)**bonus* -1)
        else:
            result.append(int(score)**bonus)
    return sum(result)

#print(solution("1S*2T*3S"))