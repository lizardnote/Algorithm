import sys
input = sys.stdin.readline
A = []

for i in range(9):
    A.append(list(map(int, input().split())))
    
max = -1
for i in range(9):
    for j in range(9):
        if A[i][j] > max:
            max = A[i][j]
            n = i +1
            m = j +1
            
print(max)
print(n, m)
        
        