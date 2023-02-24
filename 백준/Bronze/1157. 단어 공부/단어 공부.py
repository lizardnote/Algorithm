cnt = []
data = list(input().upper())
dataset = set(data)

for _ in dataset:
    cnt.append(data.count(_))

if cnt.count(max(cnt)) > 1 :
    print("?")
else:
    print(list(dataset)[cnt.index(max(cnt))])