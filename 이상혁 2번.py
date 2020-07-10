def find_three_smallest(list):
    min3 = 0 # 처음 3개의 값 중 최댓값을 찾기 위해 초기값을 0으로 설정

    for i in range(0,3): # 최댓값 찾는 for문, 최댓값을 찾아 min3에, 인덱스를 min3_index에 저장
        if(min3 < list[i]):
            min3 = list[i]
            min3_index = i
            
    index_list = [0,1,2] # 0,1,2중 최댓값의 인덱스를 뺌
    index_list.remove(min3_index) 
    
    if(list[index_list[0]]<list[index_list[1]]): # 최댓값이 아닌 나머지 두개에서 뭐가 더 작은지 판별
        min1,min2 = list[index_list[0]], list[index_list[1]]
        min1_index, min2_index = index_list[0], index_list[1]
    else:
        min2,min1 = list[index_list[0]], list[index_list[1]]
        min2_index, min1_index = index_list[0], index_list[1]
    # ------------------------------여기까진 처음 3개의 값만 비교함, min1이 가장 작음
    for i in range(3, len(list)): # 리스트 안에서의 대소비교
        if(min1 > list[i]): #min1보다 작으면 하나씩 다 밀림
            min1, min2, min3 = list[i], min1, min2
            min1_index, min2_index, min3_index = i, min1_index, min2_index
        elif(min2 > list[i]): #min2보다 작으면 2개만 밀림
            min2, min3 = list[i], min2
            min2_index, min3_index = i, min2_index
        elif(min3 > list[i]): #min3보다 작으면 3개만 
            min3 = list[i]
            min3_index = i
    return min1_index, min2_index, min3_index
