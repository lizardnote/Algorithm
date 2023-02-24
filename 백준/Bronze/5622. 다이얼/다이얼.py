import sys

NUM = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
data = list(sys.stdin.readline())
result = 0
for i in data:
    for j in NUM:
        if i in j:
            result += NUM.index(j) + 3
print(result)