def solution(numbers, hand):
    answer = ''
    pos_left, pos_right = 10, 12
    distance = [0,0]
    left = [1,4,7]
    right = [3,6,9]
    j=0
    for i in numbers:
        if(i in left):
            pos_left = i
            answer += 'L'
        elif(i in right):
            pos_right = i
            answer += 'R'
        else:
            if(i == 0):
                j = i
                i = 11
            pos1, pos2 = pos_left, pos_right
            while True:
                if(pos1 == i):
                    break
                distance[0] += 1
                if(pos1+1 == i) or (pos1-1 == i):
                    break
                else:
                    if(pos1 > i):
                        pos1 -= 3
                    else:
                        pos1 += 3                
            while True:
                if(pos2 == i):
                    break
                distance[1] += 1
                if(pos2+1 == i) or (pos2-1 == i):
                    break
                else:
                    if(pos2 > i):
                        pos2 -= 3
                    else:
                        pos2 += 3
            if(distance[0] < distance[1]):
                pos_left = i
                answer += 'L'
            elif(distance[0] != distance[1]):
                pos_right = i
                answer += 'R'
            else:
                if(hand == 'left'):
                    pos_left = i
                    answer += 'L'
                else:
                    pos_right = i
                    answer += 'R'
            distance = [0,0]
            i = j
                
    return answer
