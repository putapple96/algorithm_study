# n : 진법, 미리 구할 숫자 개수 t, 게임 참가 인원 m, 본인의 순서 p
def convert(base, n):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(base, q) + T[r]
        
def solution(n, t, m, p):
    answer = ''
    s = ""
    for i in range(t * m):
        s += convert(n, i) 
    
    my_pos = p - 1
    for i in range(t):
        answer += s[my_pos]
        my_pos += m

    return answer