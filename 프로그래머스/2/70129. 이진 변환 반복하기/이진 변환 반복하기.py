def solution(s):
    cnt_change = 0
    cnt_zero = 0
    
    while len(s) > 1 and s != '1':
        cnt_zero += s.count("0")
        s = bin(s.count("1"))[2:]
        cnt_change += 1
        
    return [cnt_change, cnt_zero]