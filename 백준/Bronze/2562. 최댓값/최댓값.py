li = []
while 1:
    try:
        n = int(input())
        li.append(n)
    except:
        break

print(max(li))
print(li.index(max(li))+1)

    