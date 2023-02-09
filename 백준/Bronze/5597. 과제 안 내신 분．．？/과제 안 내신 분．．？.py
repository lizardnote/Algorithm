li=[]
data = [i for i in range(1,31)]

while 1:
    try:
        n = int(input())
        li.append(n)
    except:
        break

diff = list(set(data)-set(li))

print(min(diff))
print(max(diff))
        