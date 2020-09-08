def isCorrect(s): # 올바른 괄호 인지 확인
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0: return False
            else:
                stack.pop()
    if len(stack) == 0: return True
    else: return False

def seperate(s):
    if s == '': return ''
    open_cnt = 0
    close_cnt = 0
    u = ''
    result = ''
    for c in s:
        if c == '(':
            open_cnt += 1
            u += c
        elif c == ')':
            close_cnt += 1
            u += c
        if open_cnt == close_cnt: break
    
    v = ''
    for j in range(len(u), len(s)):
        v += s[j]
    
    if isCorrect(u):
        result += u
        result += seperate(v)
    else:
        result = '(' + seperate(v) + ')'
        u = u[1:len(u)-1]
        #print(u)
        for c in u:
            if c == '(':
                result += ')'
            else:
                result += '('
    return result

def solution(p):
    answer = ''
    if isCorrect(p):
        return p
    answer = seperate(p)
    return answer
