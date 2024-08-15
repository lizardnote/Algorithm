def solution(x):
    
    x_li = [int(i) for i in str(x)]
    print(x_li)
    if x % sum(x_li) == 0:
        answer = True
    else:
        answer = False
        
    return answer
    