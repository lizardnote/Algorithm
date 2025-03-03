def solution(absolutes, signs):
    new_sign = []
    for x in signs :
        if x == False:
            x = -1
            new_sign.append(x)
        else:
            x = 1
            new_sign.append(x)            
        
    sum = 0
    for i in range(len(absolutes)):
        sum += new_sign[i] * absolutes[i]
        

    return sum
            
        
    answer = 123456789
    return int(True)