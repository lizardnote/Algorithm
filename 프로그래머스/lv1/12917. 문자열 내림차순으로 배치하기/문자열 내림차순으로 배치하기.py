def solution(s):
    s_li = list(s)
    s_li.sort(reverse = True)

    return "".join(s_li)