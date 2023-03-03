import sys
input = sys.stdin.readline

while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0 : 
        break
    else :
        # factor인 경우
        if b % a == 0:
            print('factor')
        elif a % b == 0:
            print('multiple')
        else : 
            print('neither')