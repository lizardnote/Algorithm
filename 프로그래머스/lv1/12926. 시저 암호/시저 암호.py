def solution(s, n):
    answer = ''
    alist = [chr(i) for i in range(ord('a'),ord('z')+1)]
    
    for i in list(s) :
        if i == " ":
            answer += " "
            continue
        else: 
            idx = alist.index(i.lower())
            idx += n
            if idx > 25 :
                idx -= 26
        
        answer = answer + alist[idx].upper() if i.isupper() else answer + alist[idx]
        
    return answer