def solution(n):
    arr = list(range(2, n+1))
    size = len(arr)
    for i in range(2, n+1):
        if arr[i-2] == 0: continue
        num = i+i
        if(num > size):
            break
        for j in range(num, n+1, i):
            arr[j-2] = 0
        
    return size - arr.count(0)
