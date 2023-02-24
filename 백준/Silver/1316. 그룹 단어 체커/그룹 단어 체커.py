n = int(input())
cnt = n

for _ in range(n):
    data = list(input())
    for j in range(0, len(data)-1):
        if data[j] == data[j+1]:
            pass
        elif data[j] in data[j+1:]:
            cnt -= 1
            break
print(cnt)
    
