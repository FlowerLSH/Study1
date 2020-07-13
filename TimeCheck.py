import time
def TimeCheck(function,list1):
    time1 = time.perf_counter()
    function(list1)
    time2 = time.perf_counter()
    return (time2-time1) * 1000
