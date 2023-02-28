n = int(input())
d = 1  #해당 층의 최댓값
cnt = 1
while d < n:  
    cnt += 1
    d = d + cnt     

if cnt % 2 == 1: #홀수층이면 오른쪽부터
    num = d - n
    print((1+num),'/',(cnt-num), sep='')
else : #짝수층이면 왼쪽부터
    num = d- n
    print((cnt-num),'/',(1+num), sep='')