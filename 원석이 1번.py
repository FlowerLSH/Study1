def vkdlsem(list,num):
    first = 0
    last = len(list)
    turn = 0
    n=0
    wprhq = 0

    while wprhq < len(list):
        wprhq = 2**n
        n = n + 1

    while turn < n:
        mid = (first + last) // 2
        if num < list[mid]:
                last = mid - 1
        elif num > list[mid]:
                first = mid + 1
        else:
            return mid
        turn += 1
    return -1

# ---------------------- 여기서부터는 테스트부분

import random

alist= []
for i in range(100000):
    num = random.randint(1,50000)
    alist.append(num)

list1 = set(alist)
alist = list(list1)
alist.sort()
a = vkdlsem(alist,14141)

if(a!=-1):
    print(a,alist[a])
else:
    print(-1)

