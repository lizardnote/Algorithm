def solution(s):
    answer = True
    
    if s.lower().count('p') == s.lower().count('y'):
        return True
    
    else:
        return False