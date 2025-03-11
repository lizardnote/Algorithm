def solution(left, right):
    # li = []
    # for i in range(left,right+1):
    #     if i % (i**(1/2)) == 0 :
    #         li.append(i*-1)
    #     else:
    #         li.append(i)
    # return sum(li)
    return sum([(-i if i%(i**(1/2)) == 0 else i) for i in range(left, right+1)])