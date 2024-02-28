def dice(lev, start):
    if lev == n:
        print(path)
        return
    else:
        for i in range(start, 7):
            path.append(i)
            dice(lev+1, i)
            path.pop()



path = []
n = 3

dice(0, 1)