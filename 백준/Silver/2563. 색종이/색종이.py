def makelist():
    p = []                         # 빈 리스트 선언
    a,b = map(int,input().split())  #색종이 왼쪽 아래 좌표 입력
    for i in range(10):              # 좌표 만들어서 리스트에 삽입(0~10까지)
        for j in range(10):           
            p.append((a+i,b+j))

    return p  # 색종이 하나의 좌표 리스트 반환

total = set()    # 빈 set 선언
n = int(input())  # 색종이 총 개수 입력
for i in range(n): # 색종이 수 만큼 반복
    p = makelist()    # 색종이 좌표 리스트 함수 값을 p로 받고
    total.update(p)    # 빈 집합에 추가

print(len(total))