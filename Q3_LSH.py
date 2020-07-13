import time
def TimeCheck(function,list1):
    time1 = time.perf_counter()
    function(list1)
    time2 = time.perf_counter()
    return (time2-time1) * 1000

def ReturnTime(function, list):
    sum = 0
    for i in range(10000):
        sum += TimeCheck(function,list)
    return sum / 10000

def MakeSorted2(list):
    empty_list = []
    list1 = list.copy()
    for i in range(len(list1)):
        min_num = min(list1)
        empty_list.append(min)
        list1.remove(min_num)
    return empty_list

def MakeSorted(list1):
    for i in range(1,len(list1)):
        for j in range(i, 0, -1):
            if(list1[j]<list1[j-1]):
                list1[j-1], list1[j] = list1[j],list1[j-1]
    return list1
