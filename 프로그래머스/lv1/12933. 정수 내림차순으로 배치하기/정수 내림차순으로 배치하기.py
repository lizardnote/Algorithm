def solution(n):
    answer= 0
    li = list(str(n))
    num_li = sorted([int(i) for i in li])
    for i in range(len(num_li)): # i는 0~5
        answer += num_li[i] * (10 ** i) 
    return answer