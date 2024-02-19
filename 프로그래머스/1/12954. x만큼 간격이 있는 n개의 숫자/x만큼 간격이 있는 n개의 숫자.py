def solution(x,n):
    answer = []
    a = 0
    for i in range(n):
        answer.append(a+x)
        a+=x
    return answer
    