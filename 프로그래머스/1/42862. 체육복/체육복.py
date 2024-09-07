# def solution(n, lost, reserve):
#     answer = 0
#     lost.sort()
#     reserve.sort()
    
#     for i in reserve:
#         temp = i-1
#         temp2 = i+1
#         if i in lost:  #여벌 가져온 학생이 체육복을 도난당한 경우
#             lost.remove(i)  #본인한테 빌려줌
#         elif temp in lost: 
#             lost.remove(temp)
#         elif temp2 in lost:
#             lost.remove(temp2)

#     answer = n - len(lost)
#     return answer

def solution(n, lost, reserve):
    # 정렬
    lost.sort()
    reserve.sort()
	
    # lost, reserve에 공통으로 있는 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
	
    # 체육복 빌려주기(나의 앞 번호부터 확인)
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    
    return n-len(lost)