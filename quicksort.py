def quick(list):
    if len(list) <= 1:
        return list

    p = list[len(list) // 2]
    less = []
    more = []
    equal = []

    for a in list :
        if a < p :
            less.append(a)
        elif a > p :
            more.append(a)
        else:
            equal.append(a)

    return quick(less) + equal + quick(more)
