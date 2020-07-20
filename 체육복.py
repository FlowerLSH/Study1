def solution(n, lost, reserve):
    new_reserve = list(set(reserve) - set(lost))
    new_lost = list(set(lost) - set(reserve))
    new_reserve.sort()
    new_lost.sort()
    answer = n - len(new_lost)
    for i in new_reserve:
        if((i-1) in new_lost):
            new_lost.remove(i-1)
            answer += 1
        elif((i+1) in new_lost):
            new_lost.remove(i+1)
            answer += 1
    return answer
