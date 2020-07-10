def find_three_smallest(list):
    min3 = 0
    index_list = [0,1,2]
    for i in range(0,3):
        if(min3 < list[i]):
            min3 = list[i]
            min3_index = i
    index_list.remove(min3_index)
    if(list[index_list[0]]<list[index_list[1]]):
        min1,min2 = list[index_list[0]], list[index_list[1]]
        min1_index, min2_index = index_list[0], index_list[1]
    else:
        min2,min1 = list[index_list[0]], list[index_list[1]]
        min2_index, min1_index = index_list[0], index_list[1]
    
    for i in range(4, len(list)):
        if(min1 > list[i]):
            min1, min2, min3 = list[i], min1, min2
            min1_index, min2_index, min3_index = i, min1_index, min2_index
        elif(min2 > list[i]):
            min2, min3 = list[i], min2
            min2_index, min3_index = i, min2_index
        elif(min3 > list[i]):
            min3 = list[i]
            min3_index = i
    return min1_index, min2_index, min3_index
