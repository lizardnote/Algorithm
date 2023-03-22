def solution(left, right):
    li = []
    for i in range(left,right+1):
        if i % (i**(1/2)) == 0: 
            li.append(-1*i)
        else:
            li.append(i)
    return sum(li)            
    
    # li = [(i if (i % (i**(1/2))==0)  else -1 * i ) for i in range(left, right+1)
    