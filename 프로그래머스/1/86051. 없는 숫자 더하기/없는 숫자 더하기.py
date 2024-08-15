def solution(numbers):
    num_set = set([i for i in range(10)])
    answer = -1
    number_set = set(numbers)
    return sum(num_set-number_set)

    