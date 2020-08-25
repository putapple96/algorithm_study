t = int(input())

def baby_gin(player_card):
    for i in range(len(player_card)):
        if player_card[i] >=3: # Triplet
            return True
        if i <= 7: # run 까지 고려할 수 있는 상황이라면
            if player_card[i] > 0 and player_card[i+1] > 0 and player_card[i+2] > 0: # run 체크
                return True
    return False

for tc in range(t):
    # 각 플레이어가 받은 카드 숫자에 따라 개수 셀 count list
    player1 = [0] * 10
    player2 = [0] * 10

    info = list(map(int, input().split()))

    game_result = 0
    for i in range(12):
        if i % 2 == 0:
            player1[info[i]] += 1
            if baby_gin(player1):
                game_result = 1
                break
        else:
            player2[info[i]] += 1
            if baby_gin(player2):
                game_result = 2
                #print("#{} 2".format(tc+1))
                break
    print("#{} {}".format(tc+1, game_result))