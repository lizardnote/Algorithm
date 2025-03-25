n = int(input())

num_list = [0,1]
a = num_list[0]
b = num_list[1]

for i in range(0,n-1):
    num_list.append(a+b)
    a = b
    b = num_list[-1]

print(num_list[n])