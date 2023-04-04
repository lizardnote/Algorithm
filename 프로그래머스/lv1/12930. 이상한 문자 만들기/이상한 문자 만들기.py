def solution(s):
    answer = ''
    word = s.split(" ")
    
    for j in range(len(word)) :
        for i in range(len(word[j])):
            answer = answer + word[j][i].upper() if (i%2 == 0) else answer + word[j][i].lower()
                
        if j != len(word)-1 : answer += ' '
            
    return answer

