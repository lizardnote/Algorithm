n = int(input())
default = 1
cnt = 0

while n > default:
    cnt += 1
    default = default + cnt*6

path =  cnt + 1
print(path)

    