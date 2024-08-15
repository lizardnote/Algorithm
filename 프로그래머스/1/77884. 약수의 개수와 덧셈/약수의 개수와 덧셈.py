def solution(left, right):
    answer = 0
    
    for num in range(left,right+1):
        
        div_list = [i for i in range(1,num+1) if num % i == 0]
       
        if len(div_list) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer