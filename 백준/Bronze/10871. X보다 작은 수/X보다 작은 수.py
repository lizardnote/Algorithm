import sys
a, b = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

filtered = list(filter(lambda x : x < b, data))
print(*filtered)