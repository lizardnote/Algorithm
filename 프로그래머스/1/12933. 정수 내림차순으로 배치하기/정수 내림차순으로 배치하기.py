def solution(n):
    temp = [i for i in str(n)]
    temp.sort(reverse=True)
    return int("".join(temp))
    