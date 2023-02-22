import sys

n,m = map(int,sys.stdin.readline().split())
data = [0]*n

for i in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    for j in range(a,b+1):
        data[j-1] = c

print(*data)