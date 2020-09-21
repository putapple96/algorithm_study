# go 배열의 값 : 해당 칸의 다음칸의 인덱스
go = [0] * 33
score = [0] * 33
# 파랑칸에 멈추지 않고 외곽으로만 도는 경우 : index 0 ~ 21
# index 21은 도착칸
# go 배열의 값은 해당 칸의 다음 칸의 index
for i in range(21):
    go[i] = i + 1

go[21] = 21 # 도착칸

go[22], go[23], go[24] = 23, 24, 25
go[25], go[26], go[27] = 26, 27, 20
go[28], go[29] = 29, 25
go[30], go[31], go[32] = 31, 32, 25

# 위의 구현에 맞추어 점수값 저장하는 score 배열 초기화
for i in range(21):
    score[i] = i * 2

score[22], score[23], score[24] = 13, 16, 19
score[25], score[26], score[27] = 25, 30, 35
score[28], score[29] = 22, 24,
score[30], score[31], score[32] = 28, 27, 26

# 분기점(파랑칸 3개) 저장
branch = dict()
branch[5] = 22
branch[10] = 28
branch[15] = 30

# 4^10의 경우에 대해 dfs를 이용하여 모두 시뮬레이션
def pick(n, ans):
    global max_ans
    # 10번 다 골랐다면,
    if n == 10:
        max_ans = max(max_ans, ans)
        return
    
    for i in range(4):
        x = horse_pos[i]
        backup_x = horse_pos[i]
        move_cnt = dice[n]
        # 파랑칸(분기점 위에 있다면)
        if x == 5 or x == 10 or x == 15:
            x = branch[x]
            # 한칸 이미 이동 했으므로
            move_cnt -= 1
        
        if x + move_cnt <= 21:
            x += move_cnt
        else:
            for _ in range(move_cnt):
                x = go[x]
        # 해당 칸에 말이 이미 존재하는데, 도착점이 아니라면. 안되는 경우이므로
        if board_temp[x] and x != 21:
            continue

        board_temp[backup_x] = 0
        board_temp[x] = 1
        horse_pos[i] = x
        pick(n+1, ans+score[x])
        # 원상 복구
        board_temp[backup_x] = 1
        board_temp[x] = 0
        horse_pos[i] = backup_x

dice = list(map(int, input().split()))
# 각각 말 4개의 위치(인덱스) 저장
horse_pos = [0] * 4
# 게임판의 상태 임시 저장(몇번 말이 존재하는지)
board_temp = [0] * 33

max_ans = 0
pick(0, 0)
print(max_ans)