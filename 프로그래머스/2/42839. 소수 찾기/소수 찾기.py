from itertools import permutations

def solution(numbers):
    make_nums = []
    
#넘버스로 조합할 수 있는 숫자들 만들기    
    for i in range(len(numbers)):
        make_nums += list(map(''.join, permutations(numbers,i+1)))        
        make_nums = [int(i) for i in make_nums]

    make_nums = sorted(list(set(make_nums)))   #set으로 중복 제거
    remove_set= [0,1]
    
    for i in make_nums:
        for j in range(2,i):
            if i % j == 0 :
                remove_set.append(i)
                break
                
    answer = [i for i in make_nums if i not in remove_set]
    print(answer)
    return len(answer)
   