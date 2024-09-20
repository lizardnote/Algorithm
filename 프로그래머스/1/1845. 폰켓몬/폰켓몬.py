def solution(nums):
    num_set = set(nums)    
    answer  = len(num_set)
    num = len(nums) // 2 
    if num < answer:
        answer = num
    
    return answer