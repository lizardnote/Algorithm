data = []
while 1:
    try:
        n = int(input())
        nn = n % 42
        data.append(nn)
    except:
        break
        
print(len(set(data)))