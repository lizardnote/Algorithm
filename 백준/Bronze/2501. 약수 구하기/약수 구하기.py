num, k = map(int,input().split())
li = []
k_num= 0 

for i in range(1, num+1):
    if k_num == k: break # 구하려는 약수 개수가 충족되면 탈출

    elif num % i == 0 : # i로 나누어서 나머지가 0이면 
        li.append(i)    # 약수 리스트에 append
        k_num += 1      # 약수 개수 count

if k > len(li) : 
    print(0)
elif k == k_num : 
    print(li[k-1])

    
    
    