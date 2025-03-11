def solution(num):
    answer = 0
    if num == 1 :
        answer = 0
        
    for i in range(0,500):
        if num == 1:
            break
        elif num % 2 == 0 :
            num = num // 2
        else : 
            num = num * 3 + 1
            
    if num != 1:
        answer = -1
    else:
        answer = i
            
    return answer
   