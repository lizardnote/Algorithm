def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)):
        multi = A[i] * B[i]    
        answer += multi
        
    return answer