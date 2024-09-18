def solution(array, commands):
    answer = []
    
    for i in commands: #[2,5,3]
        idx0 = i[0]-1
        idx1 = i[1]
        idx2 = i[2]-1
        mid_answer = array[idx0:idx1]
        answer.append(sorted(mid_answer)[idx2])
    return answer