def solution(sizes):
    
    sizes.sort(key = lambda x : x, reverse = True)
    x,y = max(sizes)
    
    for i in sizes:
        if x < max(i) :
            x = max(i)
        if y < min(i) :
            y = min(i)
        
    return x*y