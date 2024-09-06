def solution(s):
    stack  = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop() #맨 뒤의 원소를 제거
        else:
            stack.append(i)
            
    return 1 if len(stack) == 0 else 0
