num = int(input())
for i in range(num):
    k = int(input())
    n = int(input())
    under = [x for x in range(1,n+1)]

    for j in range(k):
        floor = [1]
        for jj in range(0,n-1):
            new = under[jj+1] + floor[jj]
            floor.append(new)
        under = floor
    print(under[-1])