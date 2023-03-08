def solution(s):
    s = list(s.upper())
    cnt_p, cnt_y = 0 , 0
    
    for i in s :
        if i == 'P':
            cnt_p += 1
        elif i == "Y":
            cnt_y += 1
        else:
            continue
    
    return True if cnt_p == cnt_y else False
  
