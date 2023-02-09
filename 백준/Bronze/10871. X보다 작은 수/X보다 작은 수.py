import sys
a, b = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
filtered = [x for x in data if x < b]
print(*filtered)