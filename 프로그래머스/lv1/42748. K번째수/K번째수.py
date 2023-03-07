def solution(array, commands):
    answer = []
    
    for z in commands:
        i ,j ,k = z
        i = i-1
        k = k-1
        slice = array[i:j]
        slice.sort()
        answer.append(slice[k])
        slice.clear()
    return answer