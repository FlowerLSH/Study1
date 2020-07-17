def solution(answers):
    answer_list = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    count = [0,0,0]
    answer = []
    for i in answers:
        for j in range(3):
            answer_num = answer_list[j][0]
            if(answer_num == i):
                count[j] += 1
            answer_list[j].remove(answer_num)
            answer_list[j].append(answer_num)
    
    max_score = max(count)
    for i in range(len(count)):
        if(max_score == count[i]):
            answer.append(i+1)
    return answer
