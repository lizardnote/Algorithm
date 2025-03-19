from collections import deque
    
def solution(s):
    dq = deque([0])
    for i in s:
        if i == ")":
            if dq[-1] == "(" :
                dq.pop()
            else:
                dq.append(i)
        else:
            dq.append(i)
            
    return True if len(dq)==1 else False
                