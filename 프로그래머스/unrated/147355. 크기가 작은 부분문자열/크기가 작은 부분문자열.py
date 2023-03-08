def solution(t, p):
    cnt = 0
    for i in range(len(t)-len(p)+1):
        part = t[i:i+len(p)]
        if int(part) <= int(p) :
            cnt += 1
    return cnt