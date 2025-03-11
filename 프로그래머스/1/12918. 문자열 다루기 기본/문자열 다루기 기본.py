def solution(s):
    if len(s)==4 or len(s) == 6:
        for i in s:
            if i in "0123456789" :
                answer = True
            else:
                answer = False
                break
    else:
        answer = False
                
            
    return answer