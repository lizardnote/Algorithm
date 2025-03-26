stu = [i for i in range(1,31)]

for _ in range(0,28):
    a = int(input())
    stu.remove(a)
    
print(min(stu))
print(max(stu))

