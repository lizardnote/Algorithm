import sys
num = int(input())
data = list(map(int, sys.stdin.readline().split()))
find = int(input())

print(data.count(find))
