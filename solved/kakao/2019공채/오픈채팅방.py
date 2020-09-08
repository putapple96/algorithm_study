def solution(record):
    answer = []
    user_info = {}
    for rec in record:
        info = rec.split(' ')
        if info[0] == 'Enter' or info[0] == 'Change':
            user_info[info[1]] = info[2]
    
    for rec in record:
        info = rec.split(' ')
        if info[0] == "Enter":
            message = user_info[info[1]] + "님이 들어왔습니다."
            answer.append(message)
        elif info[0] == "Leave":
            message = user_info[info[1]] + "님이 나갔습니다."
            answer.append(message)

    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
"Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(records)