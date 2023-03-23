def solution(s):
    if len(s) == 4 or len(s) == 6:
        num = [str(i) for i in range(10)]
        s = list(s)
        S = s.copy()
        for i in s:
            if i in num :
                S.remove(i)
        return True if len(S) == 0 else False

    else: return False

    