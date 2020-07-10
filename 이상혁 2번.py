def find_two_smallest(list1):
    smallest = min(list1)
    min1 = list1.index(smallest)
    list1.remove(smallest)
    next_smallest = min(list1)
    min2 = list1.index(next_smallest)
    list1.insert(min1,smallest)
    if min1<=min2:
        min2+=1
    return (min1,min2)
    
def find_sorted(list1):
    sort_list = sorted(list1)
    min1=list1.index(sort_list[0])
    min2=list1.index(sort_list[1])
    return (min1,min2)
    
def find_walkthrough(list1):
    if (list1[0]<list1[1]):
        min1, min2 = 0 ,1
    else:
        min1, min2 = 1, 0
    
    for i in range(2,len(list1)):
        if(L[i]<L[min1]):
            min2, min1 = min1, i
        elif (L[i]<L[min2]):
            min2 = i
    return (min1,min2)
