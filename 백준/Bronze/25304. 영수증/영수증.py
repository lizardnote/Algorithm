import sys

total = int(input())
n = int(input())
sum = 0

for i in range(n):
    price, count = map(int, sys.stdin.readline().split())
    sum += price * count
    
if sum == total :
    print('Yes')
else:
    print("No")