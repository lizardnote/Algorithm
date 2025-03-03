def solution(n):
    new = [x for x in str(n)]
    new.sort(reverse=True)
    
    return int(''.join(new))