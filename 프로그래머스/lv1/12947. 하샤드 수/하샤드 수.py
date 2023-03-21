def solution(x):
    answer = True
    li = list(str(x))
    intli = [int(i) for i in li]
    if x % sum(intli) == 0:
        answer = True
    else:
        answer = False
    
    return answer