def solution(a, b, n): 
    cnt = 0
    rest = 0
    
    while n >= a:
        mok = n // a
        nam = n % a
        n = mok * b + nam
        cnt += mok*b
    
    return cnt
    
