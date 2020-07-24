def solution(strings, n):
    answer = []
    index = dict()
    arr1 = []
    for i in strings:
        index[i] = i[n]
        arr1.append(i[n])
    arr = list(set(arr1))
    arr.sort()
    for j in arr:
        emp = []
        for k in index:
            if index[k] == j: emp.append(k)
        emp.sort()
        answer.extend(emp)
    
        return answer
    
    
def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    strings.sort()    
    for j in strings:
        answer.append(j[1:])
    return answer
