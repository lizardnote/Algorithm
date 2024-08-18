def solution(d, budget):
    answer = 0
    ord_list = sorted(d, reverse = False)
    
    for i in range(len(ord_list)):
        answer += ord_list[i] 
        if answer <= budget:
            continue
        else:
            i -= 1
            break
            
    return i+1