def solution(answers):
    answer = [0,0,0]
    ans = []
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if num1[i%5] == answers[i] :
            answer[0] += 1
        if num2[i%8] == answers[i] :
            answer[1] += 1
        if num3[i%10] == answers[i]:
            answer[2] += 1
    
    for i in range(3):
        if answer[i] == max(answer):
            ans.append(i+1)    
    return ans
