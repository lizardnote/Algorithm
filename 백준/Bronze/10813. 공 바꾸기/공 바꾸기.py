import sys

n,m = map(int,sys.stdin.readline().split())
data = [x for x in range(1,(n+1))]
                         
for i in range(m):
    a,b = map(int, input().split())
    c = data[(b-1)] 
    data[(b-1)] = data[(a-1)]
    data[(a-1)] =  c

print(*data)