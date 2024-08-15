def solution(price, money, count):
    tot = 0
    for i in range(1,count+1):
        tot += (price*i)

    return tot-money if tot >= money else 0