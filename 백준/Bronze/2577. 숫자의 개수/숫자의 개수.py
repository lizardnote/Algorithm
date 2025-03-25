import sys
a = int(input())
b = int(input())
c = int(input())

gop = a * b * c
num_list = list(str(gop))

for i in range(0,10):
    cnt = num_list.count(str(i))
    print(cnt)
    cnt = 0