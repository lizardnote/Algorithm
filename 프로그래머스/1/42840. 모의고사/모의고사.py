def solution(answers):
    answer = [0] * 3
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == num1[i%5]:
            answer[0] += 1
        if answers[i] == num2[i%8]:
            answer[1] += 1
        if answers[i] == num3[i%10]:
            answer[2] += 1
            
    winner = max(answer)
    person= []
    for i in range(len(answer)):
        if answer[i] == winner:
            person.append(i+1)
            
    return person
        
        
        

    
    
#     answer = [cnt1, cnt2, cnt3]
    
#     return max(answer)