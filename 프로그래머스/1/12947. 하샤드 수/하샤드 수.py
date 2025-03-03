def solution(x):
    answer = False
    if x % sum([int(x) for x in str(x)]) == 0 :
        answer = True
    
    return answer