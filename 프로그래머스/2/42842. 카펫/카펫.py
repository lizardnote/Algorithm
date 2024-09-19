# def solution(brown, yellow):
    
#     #약수 구하기 = 노랑이의 가로 세로를 구하기 위함
#     answer = []
#     garo = 0
#     sero = 0
    
#     for i in range(1,yellow+1):
#         if yellow % i == 0 :
#             garo = int(yellow/i)
#             sero = i

    
#             if garo*2 + sero*2 + 4 == brown :            
#                 answer.append(garo+2)
#                 answer.append(sero+2)
                
#         return sorted(answer, reverse = True)

    
def solution(brown, yellow):    
    answer = []
    
    yellow_x = 0
    yellow_y = 0
    
    for i in range(1, yellow+1) :
        if yellow % i == 0 :
            yellow_x = int(yellow/i)
            yellow_y = i
            if yellow_x*2 + yellow_y*2 + 4 == brown :            
                answer.append(yellow_x+2)
                answer.append(yellow_y+2)
                
                return sorted(answer, reverse = True)
    
    return answer
