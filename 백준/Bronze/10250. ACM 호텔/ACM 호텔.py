import sys

input = sys.stdin.readline
k = int(input())

for i in range(k):
    f,r,num = map(int,input().split())
    
    if num % f == 0 :  #나누어 떨어지는 경우, 맨 윗층 마지막 방에 배정
        cnt = str(num // f) #cnt는 roomnum 의 뒷자리
        if len(cnt) == 1:
            cnt = cnt.zfill(2)
        roomnum = str(f)
        
    else: #나누어 떨어지지 않는 경우
        cnt = str(num//f + 1) 
        if len(cnt) == 1:
            cnt = cnt.zfill(2)
        roomnum = str(num % f)
    print(roomnum+cnt)