cnt = int(input())
li = list(map(int, input().split()))
answer = []

for i in li:
  if i == 1 :
    cnt -= 1
  else:
    for j in range(2,i):
      if i % j == 0:
        cnt -= 1
        break

print(cnt)