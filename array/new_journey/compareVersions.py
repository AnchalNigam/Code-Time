def compareVersions(a, b):
    x = list(map(int, a.split('.')))
    y = list(map(int, b.split('.')))
    n1 = len(x)
    n2 = len(y)
    if n1 > n2:
        n = n2
    else:
        n =  n1
    for i in range(n):
        if x[i] > y[i]:
            return 1
        elif x[i] < y[i]:
            return -1
    if n == n2 and n == n1:
        return 0
    elif n == n2:
        return 1
    return -1