def solution(array, commands):
    answer = []
    
    for z in commands:
        i ,j ,k = z
        slice = array[i-1:j]
        slice.sort()
        answer.append(slice[k-1])
        slice.clear()
    return answer