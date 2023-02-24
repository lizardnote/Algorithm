data = ['c=','c-','dz=','d-','lj','nj','s=','z=']

read = input()
for i in data:
    if i in read :
        read = read.replace(i , "*")
print(len(read))
