import sys
n = int(input())

for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    mean = sum(data[1:]) / data[0]
    
    cnt = 0
    for i in data[1:]:
        if i > mean:
            cnt += 1
    per = (cnt/data[0])*100
    print('%.3f' %per + "%")