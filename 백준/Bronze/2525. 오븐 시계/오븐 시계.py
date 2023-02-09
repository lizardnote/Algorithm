import sys

H, mm = map(int, sys.stdin.readline().split())
t = int(input())

H += t//60
mm += t % 60

if mm >= 60 : 
    mm -= 60  
    H += 1
if H >= 24 :
    H -= 24
    
print(H, mm)
    
   
    