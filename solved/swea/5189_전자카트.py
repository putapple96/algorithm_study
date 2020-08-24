# 완전탐색
from itertools import permutations

t = int(input())

for tc in range(t):
    n = int(input())
    m = []
    ans = 987654321
    for _ in range(n):
        m.append(list(map(int, input().split())))
    
    mylist = []
    for i in range(1, n):
        mylist.append(i) # 입력받은 n에 따라 (방 번호 -1)한 값을 배열에 넣어줌
    
    permu = permutations(mylist) # 방번호(1번방을 제외)로 순열 생성
    for order in list(permu):
        consume = m[0][order[0]] # 1번방에서 순열 상의 그 다음방으로 가는데 소비되는 양

        for i in range(len(order)-1): # 현재 순열 내의 순서에 따라 소비량 더해나감
            cur_room = order[i]
            next_room = order[i+1]
            consume += m[cur_room][next_room]
        
        consume += m[order[-1]][0] # 다시 1번방으로 돌아오는 양 계산
        ans = min(ans, consume) # 최솟값 갱신
    
    print("#{} {}".format(tc+1,ans))