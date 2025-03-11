def solution(s):
    li_s = list(s)
    li_s.sort(reverse = True)
    return "".join(li_s)