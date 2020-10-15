def solution(people, limit):
    people.sort()
    s, e = 0, len(people) - 1
    answer = 0
    while s <= e:
        answer += 1
        if people[s] +people[e] <= limit:
            s += 1
        e -= 1
    return answer