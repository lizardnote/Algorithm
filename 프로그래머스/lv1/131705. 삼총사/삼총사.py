from itertools import combinations
def solution(number):
    answer = 0
    plist = list(combinations(number, 3))
    
    for i in plist :
        if sum(i) == 0 :
            answer += 1
            
    return answer
