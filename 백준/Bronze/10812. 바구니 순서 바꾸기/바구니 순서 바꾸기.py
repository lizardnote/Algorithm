import sys

n, m = map(int, sys.stdin.readline().split())
data = [(x+1) for x in range(n)]
change = []

for _ in range(m):
    begin, end, mid = map(int, sys.stdin.readline().split())
    for i in range(mid, (end+1), 1):
        change.append(data[(i-1)])
    for j in range(begin,mid,1):
        change.append(data[(j-1)])
    
    number = 0
    for k in range(begin,(end+1), 1):
        data[(k-1)] = change[number]
        number += 1
    change = []
        
for _ in range(len(data)):
    print(data[_], end=' ')

        
    
    