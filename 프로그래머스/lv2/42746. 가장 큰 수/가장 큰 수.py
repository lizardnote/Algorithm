def solution(numbers):
    num = [str(s) for s in numbers]
    num.sort(key = lambda x : x*3, reverse = True)
    
    return str(int(''.join(num)))