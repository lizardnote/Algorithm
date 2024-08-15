def solution(num):
    answer = -1
    
    if num == 1:
        answer = 0
    else :
        for i in range(0,500):
            if num == 1 :
                answer = i
                break
            else:
                if num % 2 ==0 :
                    num /= 2
                else : 
                    num *= 3
                    num += 1
            
    return answer