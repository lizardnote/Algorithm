def solution(n):
    answer = 0
    a = 0
    b = 1
    for i in range(2,n+1):  # n= 5       
        c = a + b         # c = 1      / 2   / 3
        a,b = b,c 
    answer = c % 1234567
    return answer