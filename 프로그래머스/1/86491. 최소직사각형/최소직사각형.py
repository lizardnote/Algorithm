def solution(sizes):
    answer = 0
    list_min = []
    list_max = []
    for a,b in sizes:
        list_min.append(min(a,b))
        list_max.append(max(a,b))
        
    return max(list_min) * max(list_max)

