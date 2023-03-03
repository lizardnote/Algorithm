a= int(input())
b = int(input())
li = []

for i in range(a,b+1):
    for j in range(2, i+1):
        if i % j == 0 :
            if j == i:
                li.append(i)
            break
            
if len(li) == 0:
    print(-1)
else:
    print(sum(li))
    print(min(li))