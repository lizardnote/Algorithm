def solution(n):
    answer = 0
    num = n ** (1/2)
    
    if num % 1 == 0:
        num += 1 
        answer = num * num
    else :
        answer = -1
   
    return answer