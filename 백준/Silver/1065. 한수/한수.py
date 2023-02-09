n = int(input())
cnt = 0

for i in range(1,n+1):
    li = list(str(i))
    if len(li) == 1 or len(li) == 2 :
        cnt += 1
    elif len(li) == 3:
        if (int(li[0]) - int(li[1])) == (int(li[1]) - int(li[2])) :
            cnt += 1
    else: cnt += 0

print(cnt)
        